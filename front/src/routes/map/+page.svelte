<script lang="ts">
    import { onMount } from "svelte";
    import Filters from "./Filters.svelte";
    import ModeSwitch from "./ModeSwitch.svelte";
    import { InitMap } from "./map";
    import Wrapper from "$lib/Wrapper.svelte";

    onMount(async () => {
        await InitMap(document.getElementById("map")!);
    });
</script>

<Wrapper>
    <main>
        <div id="map" />
        <ModeSwitch />
        <Filters />
    </main>
</Wrapper>

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
