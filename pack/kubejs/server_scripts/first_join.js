// Sky Frogs - first-launch inventory grant.
//
// Modern skyblock packs grant starter items via a first-join guard rather than
// placing a chest on the island. We mirror the verified KubeJS 2101 pattern from
// the Sky Bees Reborn reference: a one-shot guard stored in player.persistentData.
//
// The grant is just the quest book now. Every bootstrap item - saplings, the second
// water source, lava for the cobble generator, food - is handed out as an early quest
// reward instead, so the questbook drives the entire opening. No frog here either: the
// breeding pair (a Bottle of Cave Frog Frogspawn) is the Welcome chapter's completion reward.

PlayerEvents.loggedIn(event => {
  const { player } = event
  const data = player.persistentData

  if (data.contains('skyfrogs:firstJoin')) return
  data.putBoolean('skyfrogs:firstJoin', true)

  // The guided path, in hand. (Auto-open on first join is an FTB Quests setting,
  // not a KubeJS one - configured separately in the quest book data.)
  player.give(Item.of('ftbquests:book'))

  player.tell(Text.green('Welcome to Sky Frogs. Open your quest book - the frogs do the mining around here.'))
})
