// Sky Frogs - first-launch inventory grant.
//
// Modern skyblock packs grant starter items via a first-join guard rather than
// placing a chest on the island. We mirror the verified KubeJS 2101 pattern from
// the Sky Bees Reborn reference: a one-shot guard stored in player.persistentData.
//
// The kit is the Tier 0 bootstrap: saplings for a tree farm, plus the second water
// source + lava for a cobblestone generator. No food in the grant - that comes from
// early quest rewards. No frog here either: the breeding pair (a Bottle of Cave Frog
// Frogspawn) is the Welcome quest's completion reward.

PlayerEvents.loggedIn(event => {
  const { player } = event
  const data = player.persistentData

  if (data.contains('skyfrogs:firstJoin')) return
  data.putBoolean('skyfrogs:firstJoin', true)

  player.give(Item.of('minecraft:oak_sapling', 6))
  player.give(Item.of('minecraft:water_bucket'))
  player.give(Item.of('minecraft:lava_bucket'))

  // The guided path, in hand. (Auto-open on first join is an FTB Quests setting,
  // not a KubeJS one - configured separately in the quest book data.)
  player.give(Item.of('ftbquests:book'))

  player.tell(Text.green('Welcome to Sky Frogs. Open your quest book - the frogs do the mining around here.'))
})
