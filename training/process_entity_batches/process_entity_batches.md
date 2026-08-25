## Process Entity Batches

Build an entity-management system for a workshop. It stores **Material** and **Machine** entities and processes a batch without stopping when an operation fails.


# *Entities*
Every entity has a unique string **entity_id** and a non-empty **name**.

-   **Material(entity_id, name, quantity)** requires a non-negative integer quantity.
-   **Machine(entity_id, name, condition)** requires an integer condition from **0** through **100**.

Each entity must provide an **update(changes)** method. Only **name** and the entity's type-specific field may be updated. Reject unknown fields and invalid values.


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
**BatchProcessor.process(operations)** accepts a list of operation dictionaries. Supported actions are **create**, **update**, **remove**, and **summary**.

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