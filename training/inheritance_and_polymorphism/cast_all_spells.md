
# Cast All Spells (Inheritance & Polymorphism)

**Complete the small spell system using classes, inheritance, and polymorphism.**

You will work with three classes and one helper function:

- `Spell` (base class)
- `FireSpell` (inherits from `Spell`)
- `IceSpell` (inherits from `Spell`)
- `cast_all(spells, base_power)` (uses polymorphism)


## Requirements

1. `Spell` base class

Create a base class `Spell` with:

- An `__init__(self, name, mana_cost)` method that stores the two values on the instance.
    - `name`: the spell's name (string)
    - `mana_cost`: how much mana it costs to cast (number)
- A method `cast(self, base_power)` that does not implement any real logic, it should just raise a `NotImplementedError`.

This base class is not meant to be used directly. Its `cast` method exists so subclasses can override it.


2. `FireSpell` subclass

Create a class `FireSpell` that **inherits** from `Spell`.

- Its `__init__(self, name, mana_cost)` should call the parent (`Spell`) constructor so `name` and `mana_cost` are set correctly.
    - Use `super().__init__(name, mana_cost)` to do this.
- Override `cast(self, base_power)` so that it:

    - Calculates `damage` as `base_power + 10`.
    - Returns a string in this exact format:
        > "Fire spell '<name>' hits for <damage> damage!"
      Where `<name>` is the spell's name and `<damage>` is the calculated number.


3. `IceSpell` subclass

Create a class `IceSpell` that inherits from `Spell`.

- Its `__init__(self, name, mana_cost)` should also call the parent constructor with `super().__init__(name, mana_cost)`.

- Override `cast(self, base_power)` so that it:

    - Calculates `damage` as `base_power + 5`.
    - Returns a string in this exact format:
        > "Ice spell '<name>' hits for <damage> damage!"


4. `cast_all(spells, base_power)` function

Complete the `cast_all` function.

- `spells` is a list of spell objects (`FireSpell` or `IceSpell`).
- `base_power` is a number.
- The function should:
    1. Create an empty list for results.
    2. Loop over each spell in `spells`.
    3. Call the spell's `cast(base_power)` method.
    4. Append the returned string to the results list.
    5. Return the results list at the end.


**Important**: `cast_all` should not care about which specific subclass it is using. It should just call `cast` on each spell object. This is *<polymorphism>*: different spell types implement cast in their own way, but `cast_all` calls them the same way.


## Examples

```
fire = FireSpell("Flame Burst", 20)
ice = IceSpell("Frost Bite", 15)

print(fire.cast(30))
# "Fire spell 'Flame Burst' hits for 40 damage!"

print(ice.cast(30))
# "Ice spell 'Frost Bite' hits for 35 damage!"

spells = [fire, ice]
results = cast_all(spells, 25)
print(results)
# [
#   "Fire spell 'Flame Burst' hits for 35 damage!",
#   "Ice spell 'Frost Bite' hits for 30 damage!",
# ]
```

## Edge cases

- If `spells` is an empty list, `cast_all` should return an empty list [].
- You can assume `base_power` is always a number.

Focus on:

- Using `class` inheritance (`FireSpell(Spell)` and `IceSpell(Spell)`).
- Calling the parent constructor with `super().__init__`.
- Overriding the `cast` method in each subclass.
- Using polymorphism in `cast_all` by calling `cast` on each spell without checking its type.