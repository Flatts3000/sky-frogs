// Sky Frogs - gate Industrial Foregoing plastic behind the Bog plastic-frog.
//
// IF makes plastic with a single smelting recipe (id industrialforegoing:plastic):
//   industrialforegoing:dryrubber  ->  industrialforegoing:plastic
// Removing it makes the Bog plastic Froglight (configurable_froglight_plastic, which
// stays) the ONLY source of plastic - so progressing Industrial Foregoing requires
// finishing the Bog tier. Removed by id, NOT by output, so the froglight smelt survives.
//
// c:plastics contains only industrialforegoing:plastic, so this one removal is the
// whole gate (verify in-game that nothing else yields plastic).
ServerEvents.recipes(event => {
  if (Platform.isLoaded('industrialforegoing')) {
    event.remove({ id: 'industrialforegoing:plastic' })
  }
})
