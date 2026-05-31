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

// Representative slice of the Good Food Loot Crate (reward_tables/7F00D00000000001.snbt):
// the 5 feasts + a few dishes. If Farmers Delight drops/renames one, the crate would grant
// an empty slot - this catches it without re-listing all 32.
const GOOD_FOOD_CANARIES = [
  'shepherds_pie', 'honey_glazed_ham', 'gleaming_salad', 'roast_chicken', 'stuffed_pumpkin',
  'noodle_soup', 'squid_ink_pasta', 'baked_cod_stew'
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

  // 3. Milk buckets carry NO craft remainder (the bucket-dupe fix held). NeoForge 1.21
  //    exposes this as ItemStack.getCraftingRemainingItem() - NOT getCraftingRemainder
  //    (confirmed against neoforge IItemStackExtension). Checked per-variant, so a
  //    regex-modify miss on any single variant surfaces as a real failure here.
  CANARY_VARIANTS.forEach(v => {
    check('no bucket dupe (milk craft-remainder empty): ' + v, () => {
      const rem = Item.of('productivefrogs:' + v + '_slime_milk_bucket').getCraftingRemainingItem()
      return rem == null || rem.isEmpty()
    })
  })

  // 4. The Good Food Loot Crate's contents resolve as real items. Representative sample
  //    (the table has 32; this catches a Farmers Delight pin drift that would rename/remove
  //    a food and leave the crate granting empty slots). One canary per invariant.
  GOOD_FOOD_CANARIES.forEach(food => {
    check('good food crate item exists: ' + food, () =>
      !Item.of('farmersdelight:' + food).isEmpty())
  })

  fails.forEach(name => source.sendSystemMessage(Text.red('FAIL: ' + name)))
  const total = pass + fails.length
  const summary = 'Sky Frogs self-test: ' + pass + '/' + total + ' passed'
  source.sendSystemMessage(fails.length === 0 ? Text.green(summary)
                                              : Text.yellow(summary + ' (' + fails.length + ' failed)'))
}
