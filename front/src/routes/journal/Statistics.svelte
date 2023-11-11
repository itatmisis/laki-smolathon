<script lang="ts">
    import type { JournalEntry } from "$lib/core/journal";
    import { place } from "$lib/core/places";
    import StatEntry from "./StatEntry.svelte";

    export let journal: JournalEntry[];

    let data = [0, 0, 0, 0];
    for (const entry of journal) {
        let _place = place(entry.id_location);
        _place.then(x => data[x.id_category - 1] += 1);
    }
</script>

<div>
    <p class="overall">
        Вы посетили <mark>{journal.length}</mark> Смоленских мест<br />
        Заполнили дневник для <mark>0</mark> из них<br />
    </p>
    <div class="categories">
        <StatEntry category="Памятники" count={data[0]} />
        <StatEntry category="История" count={data[1]} />
        <StatEntry category="Церкви" count={data[2]} />
        <StatEntry category="Музеи" count={data[3]} />
    </div>
</div>

<style lang="scss">
    .overall {
        font-size: 15px;
        > mark {
            background-color: var(--white1);
            padding: 2px 8px;
            border-radius: 8px;
        }
        margin-bottom: 8px;
    }
    .categories {
        display: flex;
        flex-wrap: wrap;
        gap: 4px;
    }
</style>
