<script>
    import ProfileInfo from "../ProfileInfo.svelte";
    import ProgressCard from "./ProgressCard.svelte";
    import Statistics from "./Statistics.svelte";
</script>

<header>
    <ProfileInfo name="Ivan Pirogov" />
</header>
<hr />
<div class="main">
    <Statistics />
    {#each [0, 1, 2, 3, 4] as i}
        <ProgressCard
            title="Собор святой Богородицы"
            address1="ул. Клюшкина, д. 106"
            address2="137568, Смоленская область, г. Смоленск"
        />
    {/each}
</div>

<style lang="scss">
    header {
        margin: 0 20px;
        display: flex;
        flex-direction: column;
    }
    hr {
        margin: 20px 0;
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
