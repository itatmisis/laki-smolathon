<script>
    import Icon from "$lib/Icon.svelte";
    import Wrapper from "$lib/Wrapper.svelte";
    import ProgressCard from "./ProgressCard.svelte";
    import Search from "./Search.svelte";
    import Statistics from "./Statistics.svelte";

    let search = "";
</script>

<Wrapper>
    <header>
        <Search bind:value={search} placeholder="Найти дневник" />
        <button>
            <Icon kind="filter" />
        </button>
    </header>
    <div class="main">
        <Statistics />
        {#each [0, 1, 2, 3, 4] as i}
            <ProgressCard
                title="Собор святой Богородицы"
                address1="ул. Клюшкина, д. 106"
                address2="137568, Смоленская область, г. Смоленск"
                category={"Церкви"}
            />
        {/each}
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
