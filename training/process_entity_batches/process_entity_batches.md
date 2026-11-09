## Process Entity Batches

Build an entity-management system for a workshop. It stores **Material** and **Machine** entities and processes a batch without stopping when an operation fails.


# *Entities*
Every entity has a unique string `entity_id` and a non-empty `name`.

-   `Material(entity_id, name, quantity)` requires a non-negative integer quantity.
-   `Machine(entity_id, name, condition)` requires an integer condition from **0** through **100**.

Each entity must provide an `update(changes)` method. Only `name` and the entity's type-specific field may be updated. Reject unknown fields and invalid values.


# *Collection*
Complete **EntityCollection** with these methods:

-   **create(entity)** adds an entity. Reject duplicate IDs.
-   **get(entity_id)** returns the matching entity. Reject missing IDs.
-   **update(entity_id, changes)** updates the matching entity.
-   **remove(entity_id)** removes and returns the matching entity.
-   **summary()** returns:
        *total*: total entities
        *materials*: number of materials
        *machines*: number of machines
        *material_units*: sum of all material quantities
        *average_machine_condition*: integer average condition, or **0** when there are no machines

Use integer division for the average, so conditions **80** and **91** have an average of **85**.


# *Batch Processor*
**BatchProcessor.process(operations)** accepts a list of operation dictionaries. Supported actions are `create`, `update`, `remove`, and `summary`.

Return one result dictionary for every operation, in the same order:

-   Successful changes: **{"ok": True, "action": action, "id": entity_id}**
-   Successful summaries: **{"ok": True, "action": "summary", "summary": summary}**
-   Failed operations: **{"ok": False, "action": action, "error": message}**

The required error messages are:

-   duplicate entity: <id>
-   entity not found: <id>
-   invalid name
-   invalid quantity
-   invalid condition
-   unknown field: <field>
-   unknown action: <action>

A failed operation must not change the collection, and processing must continue with the rest of the batch.


Boots discussion snippet:
Look at how the test file uses your classes:

{"action": "create", "entity": Material("mat-1", "Steel", 12)},

This line does two things in sequence: first, `Material("mat-1", "Steel", 12)` constructs a brand-new Material object by calling Material.__init__. That object is then handed to your BatchProcessor, which will eventually call `EntityCollection.create(entity)` with it. There is no database, no file, no prior state — everything starts empty in EntityCollection.__init__ and only exists because a batch operation created it.

"How do we know the format of incoming requests?"

The test file is your specification for the shape of the data. Every operation is a dictionary with an "action" key, plus whatever extra keys that action needs ("entity" for create, "id"/"changes" for update, "id" for remove). You don't need to guess — the lesson description and the test cases together define the exact contract your BatchProcessor.process must honor.
ou're not meant to reverse-engineer requirements by reading test internals — the lesson description at the top is supposed to be your primary spec (entities, fields, validation rules, error messages, EntityCollection methods, BatchProcessor behavior).

That said, looking at test cases is a completely legitimate and encouraged strategy for a Training Grounds challenge like this, especially when the prose description leaves room for interpretation. For example, the description says operations are "a list of operation dictionaries" but doesn't spell out every key name — that's exactly the kind of gap where peeking at the test file to see {"action": "create", "entity": ...} versus {"action": "update", "id": ..., "changes": ...} is fair game. You're not cheating by doing that; you're just confirming the exact contract.
