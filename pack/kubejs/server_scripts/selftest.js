// Sky Frogs - in-game runtime self-test: /sf_selftest. Layer 2 of docs/quest_testing.md.
//
// The static validator (tools/validate_quests.py) cannot see mod RUNTIME behavior. These
// canaries do: run /sf_selftest (op level 2) after a /reload to confirm the fixes held -
// per-variant items still exist (no "Missing Item" regression on a PF bump) and Slime Milk
// buckets no longer leave a bucket craft-remainder (the dupe fix). One canary per invariant,
// not exhaustive coverage.
//
// Defensive by design: every assertion is wrapped, so an API mismatch reports a FAIL line
// instead of breaking the server. If a check reports "(threw: ...)", the assertion's API
// needs adjusting, not the pack.

ServerEvents.commandRegistry(event => {
  const { commands: Commands } = event
  event.register(
    Commands.literal('sf_selftest')
      .requires(src => src.hasPermission(2))
      .executes(ctx => {
        runSelfTest(ctx.source)
        return 1
      })
  )
})

// Representative variants spanning every shipped tier, plus the infuser-only steel variant.
const CANARY_VARIANTS = [
  'iron', 'copper', 'gold', 'coal', 'redstone', 'steel',           // Cave
  'lapis', 'tuff', 'amethyst', 'emerald', 'diamond',               // Geode
  'dirt', 'mud', 'clay_ball', 'mycelium', 'plastic', 'pink_slime', // Bog
  'prismarine'                                                     // Tide (first variant)
]

function runSelfTest(source) {
  let pass = 0
  const fails = []
  const check = (name, fn) => {
    try {
      if (fn()) pass++
      else fails.push(name)
    } catch (e) {
      fails.push(name + ' (threw: ' + e + ')')
    }
  }

  // 1. Per-variant Slime Milk buckets exist (catch PF-version / id-drift regressions).
  CANARY_VARIANTS.forEach(v => {
    check('milk bucket exists: ' + v, () =>
      !Item.of('productivefrogs:' + v + '_slime_milk_bucket').isEmpty())
  })

  // 2. The Froglight item exists.
  check('configurable_froglight exists', () =>
    !Item.of('productivefrogs:configurable_froglight').isEmpty())

  // 3. Milk buckets carry NO craft remainder (the bucket-dupe fix held).
  CANARY_VARIANTS.forEach(v => {
    check('no bucket dupe (milk craftRemainder empty): ' + v, () => {
      const rem = Item.of('productivefrogs:' + v + '_slime_milk_bucket').getCraftingRemainder()
      return rem == null || rem.isEmpty()
    })
  })

  fails.forEach(name => source.sendSystemMessage(Text.red('FAIL: ' + name)))
  const total = pass + fails.length
  const summary = 'Sky Frogs self-test: ' + pass + '/' + total + ' passed'
  source.sendSystemMessage(fails.length === 0 ? Text.green(summary)
                                              : Text.yellow(summary + ' (' + fails.length + ' failed)'))
}
