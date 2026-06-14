// Sky Frogs - first-launch inventory grant.
//
// Modern skyblock packs grant starter items via a first-join guard rather than
// placing a chest on the island. We mirror the verified KubeJS 2101 pattern from
// the Sky Bees Reborn reference: a one-shot guard stored in player.persistentData.
//
// The first-join grant is just the quest book. Every bootstrap item - saplings, the
// second water source, lava for the cobble generator, food - is handed out as an early
// quest reward instead, so the questbook drives the entire opening. No frog here either:
// the breeding pair (a Bottle of Cave Frog Eggs) is the Welcome chapter's completion reward.
//
// The Productive Frogs field guide (a Patchouli book, PF 1.21+) is granted under its OWN
// guard, NOT the first-join one, so that players who already joined before the book existed
// still receive it once on their next login - "every player gets it when they start."
// The book is also craftable (vanilla book + slime ball -> productivefrogs:guide_book),
// so a lost copy is replaceable.

PlayerEvents.loggedIn(event => {
  const { player } = event
  const data = player.persistentData

  // First-join grant: the quest book (the guided path, in hand).
  // (Auto-open on first join is an FTB Quests setting, not a KubeJS one.)
  if (!data.contains('skyfrogs:firstJoin')) {
    data.putBoolean('skyfrogs:firstJoin', true)
    player.give(Item.of('ftbquests:book'))
    player.tell(Text.green('Welcome to Sky Frogs. Open your quest book - the frogs do the mining around here.'))
  }

  // One-time guide-book grant for EVERY player (new or returning). Separate guard so
  // pre-existing saves get it once too. Inert if Patchouli somehow is not loaded.
  if (!data.contains('skyfrogs:guideBookGranted')) {
    data.putBoolean('skyfrogs:guideBookGranted', true)
    if (Platform.isLoaded('patchouli')) {
      player.give(Item.of('patchouli:guide_book[patchouli:book="productivefrogs:guide"]'))
      player.tell(Text.green('A Productive Frogs field guide has been added to your inventory - flip through it any time.'))
    }
  }
})
