<script lang="ts">
    import Icon from "$lib/Icon.svelte";
    import Wrapper from "$lib/Wrapper.svelte";
    import { journal, type JournalEntry } from "$lib/core/journal";
    import { place } from "$lib/core/places";
    import ProgressCard from "./ProgressCard.svelte";
    import Search from "./Search.svelte";
    import Statistics from "./Statistics.svelte";

    let search = "";
    let _journal: Promise<JournalEntry[]> = journal();
</script>

<Wrapper>
    <header>
        <Search bind:value={search} placeholder="Найти дневник" />
        <button>
            <Icon kind="filter" />
        </button>
    </header>
    <div class="main">
        {#await _journal then _journal}
            <Statistics journal={_journal}/>
            {#each _journal as entry}
                {@const _place = place(entry.id_location)}
                {#await _place then _place}
                    <ProgressCard
                        title={_place.name}
                        address1={_place.address.line1}
                        address2={_place.address.line2}
                        category={_place.category}
                    />
                {/await}
            {/each}
        {/await}
    </div>
</Wrapper>

<style lang="scss">
    header {
        margin: 20px;
        gap: 8px;
        display: flex;
        button {
            flex: 0 0 56px;
            height: 56px;
            background-color: var(--white1);
            border: none;
            border-radius: 8px;
            --icon-size: 24px;
            padding: 16px;
        }
    }
    .main {
        flex: 1 0 10px;
        margin: 0 20px;
        gap: 12px;
        display: flex;
        flex-direction: column;
        overflow-y: scroll;
    }
</style>
