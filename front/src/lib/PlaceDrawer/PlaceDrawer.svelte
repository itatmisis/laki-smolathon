<script lang="ts">
    import { CupertinoPane, type CupertinoSettings } from "cupertino-pane";
    import CategoryChip from "$lib/CategoryChip.svelte";
    import PlaceHeader from "$lib/PlaceHeader.svelte";
    import { onMount } from "svelte";
    import Content from "./Content.svelte";
    import Tabs from "./Tabs.svelte";

    onMount(async () => {
        let settings: CupertinoSettings = {
            bottomClose: true
        };
        let myPane = new CupertinoPane(".cupertino-pane", settings);
        await myPane.present({ animate: true });
    });
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
    <Tabs/>
    <Content/>
</div>

<style lang="scss">
    .cupertino-pane {
        display: flex;
        flex-direction: column;
        gap: 8px;
        padding: 20px;
    }
    header {
        display: flex;
        flex-direction: column;
        align-items: start;
    }
</style>
