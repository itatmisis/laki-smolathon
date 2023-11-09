<script>
    import ProfileInfo from "../ProfileInfo.svelte";
    import ProgressCard from "./ProgressCard.svelte";
    import Statistics from "./Statistics.svelte";
</script>

<section>
    <ProfileInfo name="Ivan Pirogov" />
    <hr/>
    <Statistics/>
    <div>
        {#each [0, 1, 2, 3, 4] as i}
            <ProgressCard title="Собор святой Богородицы" address1="ул. Клюшкина, д. 106" address2="137568, Смоленская область, г. Смоленск" />
        {/each}
    </div>
</section>

<style lang="scss">
    section {
        flex: 1;
        margin: 20px;
        display: flex;
        flex-direction: column;
        gap: 20px;
        max-height: calc(100vh - 60px - 2 * 20px);
        div {
            display: flex;
            flex-direction: column;
            gap: 20px;
            overflow-y: scroll;
        }
        hr {
            margin: 0 -20px;
        }
    }
</style>
