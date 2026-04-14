# Game Design

## High Concept

Run a small neighborhood shop over a series of days. Each day mixes light management decisions with visual novel scenes, customer relationships, and a slow-building mystery.

## Initial Prototype Scope

The first playable build should cover Day 1 only.

Required Day 1 loop:

1. Start the morning with initial stats.
2. Review shop inventory.
3. Serve recurring customers.
4. Make at least one meaningful choice involving money, stock, reputation, or stress.
5. Close the shop and summarize the day.

## Core Stats

### Cash

Cash measures shop money. It should increase from sales and decrease from restocking, favors, mistakes, or special choices.

### Inventory

Inventory starts as a simple integer count. Later builds may split it into categories such as snacks, household goods, remedies, and oddities.

### Reputation

Reputation measures neighborhood trust. Helpful, patient, and generous decisions can increase it. Rude, careless, or exploitative decisions can lower it.

### Stress

Stress measures the player character's pressure. Taking on too much, losing money, or dealing with strange events can increase it. Calm choices and successful outcomes can reduce it.

## Day 1 Target Values

Suggested starting values:

- Cash: 80
- Inventory: 10
- Reputation: 0
- Stress: 0

## Prototype Interaction Ideas

- A regular customer wants credit until tomorrow.
- A nervous kid asks for something not normally stocked.
- A neighbor shares gossip about lights in the closed laundromat.
- A late customer arrives after the sign is flipped to closed.

## Design Constraints

- Keep mechanics readable in Ren'Py script.
- Avoid complex economy simulation in the first milestone.
- Every stat change should be shown to the player in clear prose.
- Mystery elements should be subtle on Day 1.

