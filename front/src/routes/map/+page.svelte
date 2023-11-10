<script lang="ts">
    import { onMount } from "svelte";
    import Filters from "./Filters.svelte";
    import ModeSwitch from "./ModeSwitch.svelte";
    import { InitMap } from "./map";

    onMount(async () => {
        await InitMap(document.getElementById("map")!);
    });
</script>

<main>
    <div id="map" />
    <ModeSwitch />
    <Filters />
</main>

<style lang="scss">
    main {
        --gap: 10px;

        flex: 1;
        position: relative;
        align-self: stretch;

        #map {
            width: 100%;
            height: 100%;
        }
    }
</style>
