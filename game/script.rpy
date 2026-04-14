define p = Character("You")
define vale = Character("Mrs. Vale")
define nico = Character("Nico")
define rafi = Character("Rafi")
define late = Character("Late Customer")

image bg shop morning = Solid("#3f5747")
image bg shop afternoon = Solid("#6a6853")
image bg shop night = Solid("#1f2524")

default cash = 80
default inventory = 10
default reputation = 0
default stress = 0
default nico_credit = False
default odd_item_seen = False

screen shop_stats():
    zorder 100
    frame:
        align (0.02, 0.02)
        padding (12, 8)
        vbox:
            spacing 2
            text "Cash: $[cash]" size 20
            text "Inventory: [inventory]" size 20
            text "Reputation: [reputation]" size 20
            text "Stress: [stress]" size 20

label start:
    show screen shop_stats
    scene bg shop morning

    "The bell over the door gives one tired chime when you unlock the market."
    "Morning light slips between the snack racks, the register tape, and the handwritten sign taped beside the counter."

    p "Cash box has eighty dollars. Ten good items on the shelf. Enough for a normal day, if the day stays normal."

    "You flip the sign to OPEN."

    menu:
        "Before the rush, what do you check first?"

        "Count the shelf stock again.":
            $ stress -= 1
            if stress < 0:
                $ stress = 0
            "You count slowly: canned coffee, instant noodles, batteries, cough drops, soap, and the usual emergency chocolate."
            "The numbers match. That helps."

        "Open the register and trust yesterday's count.":
            $ stress += 1
            "You decide not to count twice. The drawer opens with a click that sounds a little too loud in the empty shop."

    "A cane taps twice outside. Mrs. Vale enters before the bell finishes ringing."

    vale "Tea, batteries, and whatever rumor you have on sale."
    p "Fresh out of rumors."
    vale "Then I will take the batteries and a warning. The laundromat lights were on again after midnight."

    menu:
        "Mrs. Vale sets exact change on the counter."

        "Ask about the laundromat.":
            $ cash += 6
            $ inventory -= 1
            $ reputation += 1
            "You bag the batteries and lean closer."
            p "On how late?"
            vale "Late enough that no one living should need quarters."
            "She smiles like she has given you a coupon."
            "Cash +6. Inventory -1. Reputation +1."

        "Keep the line moving.":
            $ cash += 6
            $ inventory -= 1
            $ stress += 1
            "You ring up the batteries and wish her a good morning."
            vale "Efficient. Not curious. Dangerous combination."
            "Cash +6. Inventory -1. Stress +1."

    scene bg shop afternoon
    "By lunch, the market smells like coffee, cardboard, and rain that has not started yet."
    "Nico hurries in with his hood up, though the sky outside is still clear."

    nico "Do you have moon salt?"
    p "I have table salt."
    nico "My aunt said it would be behind the cough drops."

    "You check the shelf. Behind the cough drops sits a small blue packet with no price sticker."
    $ odd_item_seen = True

    menu:
        "Nico watches the packet like it might run."

        "Sell it for a dollar and pretend this is normal.":
            $ cash += 1
            $ inventory -= 1
            $ reputation += 1
            $ stress += 1
            "You slide the packet into a paper bag."
            nico "She said you would understand."
            p "I absolutely do not."
            "Cash +1. Inventory -1. Reputation +1. Stress +1."

        "Give it to Nico on credit.":
            $ inventory -= 1
            $ reputation += 2
            $ stress += 1
            $ nico_credit = True
            nico "I can bring money tomorrow."
            p "Bring an explanation too."
            "Inventory -1. Reputation +2. Stress +1."

        "Refuse and put it under the counter.":
            $ reputation -= 1
            $ stress += 2
            nico "Please. She said before sundown."
            p "Then she can come before sundown."
            "Nico leaves without looking back."
            "Reputation -1. Stress +2."

    "Rafi arrives with a damp delivery manifest and two crates of ordinary stock."

    rafi "Road by the laundromat is blocked. No cones. No workers. Just a sign that says COME BACK YESTERDAY."
    p "That's not a real traffic sign."
    rafi "That is what I told it."

    menu:
        "Rafi can leave both crates, but the invoice is due now."

        "Buy both crates for $30." if cash >= 30:
            $ cash -= 30
            $ inventory += 6
            $ stress -= 1
            if stress < 0:
                $ stress = 0
            "You sign the invoice. The shelves look less nervous."
            "Cash -30. Inventory +6. Stress -1."

        "Buy one crate for $16." if cash >= 16:
            $ cash -= 16
            $ inventory += 3
            "You take the essentials and promise to call if tomorrow looks better."
            "Cash -16. Inventory +3."

        "Pass on the delivery.":
            $ reputation -= 1
            $ stress += 1
            rafi "Your call. But folks notice empty shelves before they notice full hearts."
            "Reputation -1. Stress +1."

    scene bg shop night
    "At closing, the rain finally comes."
    "You turn the sign to CLOSED. The bell rings anyway."

    late "Do you still have what Nico asked for?"

    if odd_item_seen:
        "The late customer does not drip rain on the floor."
    else:
        "For one second, you cannot remember why the question makes your stomach tighten."

    menu:
        "The shop is closed."

        "Tell the truth.":
            if nico_credit:
                $ reputation += 1
                $ stress += 1
                p "Nico has it."
                late "Good. Then tonight may pass politely."
                "Reputation +1. Stress +1."
            else:
                $ stress += 1
                p "I saw it. I did not sell it."
                late "Then keep it wrapped. Do not open it after midnight."
                "Stress +1."

        "Say you do not know.":
            $ stress += 2
            late "That is rarely true in a shop this small."
            "The bell rings again when they leave, though the door never moves."
            "Stress +2."

        "Ask what moon salt is.":
            $ reputation += 1
            $ stress += 2
            late "A courtesy. A boundary. A thing people remember only when they need one."
            "Reputation +1. Stress +2."

    jump day_one_summary

label day_one_summary:
    scene bg shop night
    hide screen shop_stats

    "You count the drawer, lock the front door, and write the day's numbers on the back of an old receipt."

    "Day 1 Summary"
    "Cash: $[cash]"
    "Inventory: [inventory]"
    "Reputation: [reputation]"
    "Stress: [stress]"

    if stress >= 4:
        "Your shoulders ache by the time the lights go out."
    elif reputation >= 3:
        "For a first day, the neighborhood seems willing to give you a chance."
    else:
        "The shop is still standing. Tonight, that counts."

    "Somewhere down the block, a laundromat sign buzzes against the rain."
    "End of Day 1 prototype."

    return

