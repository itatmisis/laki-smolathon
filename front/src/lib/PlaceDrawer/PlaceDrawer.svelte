<script lang="ts">
    import { CupertinoPane, type CupertinoSettings } from "cupertino-pane";
    import CategoryChip from "$lib/CategoryChip.svelte";
    import PlaceHeader from "$lib/PlaceHeader.svelte";
    import { onMount } from "svelte";
    import Description from "./Description.svelte";
    import Tabs from "./Tabs.svelte";
    import Controls from "./Controls.svelte";
    import Reviews from "./Reviews.svelte";

    onMount(async () => {
        let settings: CupertinoSettings = {
            bottomClose: true
        };
        let myPane = new CupertinoPane(".cupertino-pane", settings);
        await myPane.present({ animate: true });
    });

    let type: "mini" | "info" | "reviews" = "mini";
</script>

<div class="cupertino-pane">
    <header>
        <CategoryChip category="Собор" />
        <PlaceHeader
            title="Собор святой Богородицы"
            address1="ул. Клюшкина, д. 106"
            address2="137568, Смоленская область, г. Смоленск"
        />
    </header>
    <Tabs bind:type />
    {#if type == "mini"}
        <Controls main_button="route" />
    {:else if type == "info"}
        <Description />
        <Controls main_button="route" />
    {:else if type == "reviews"}
        <Reviews />
        <Controls main_button="review" />
    {/if}
</div>

<style lang="scss">
    .cupertino-pane {
        display: flex;
        flex-direction: column;
        gap: 8px;
        padding: 20px;
        background-color: #f0f0fb;
    }
    header {
        background-color: white;
        display: flex;
        flex-direction: column;
        align-items: start;
        margin: -20px;
        padding: 20px;
        margin-bottom: 0;
        padding-bottom: 10px
    }
</style>
