<script lang="ts">
    import { CupertinoPane, type CupertinoSettings } from "cupertino-pane";
    import CategoryChip from "$lib/CategoryChip.svelte";
    import PlaceHeader from "$lib/PlaceHeader.svelte";
    import { onMount } from "svelte";
    import Description from "./Description.svelte";
    import Tabs from "./Tabs.svelte";
    import Controls from "./Controls.svelte";
    import Reviews from "./Reviews.svelte";
    import type { Place } from "$lib/core/places";

    export let place: Place;

    let pane: CupertinoPane;
    onMount(async () => {
        let settings: CupertinoSettings = {
            bottomClose: true,
            events: {
                onDidDismiss: () => {
                    let elements = document.querySelectorAll(".cupertino-pane");
                    for (const element of elements) {
                        element.parentElement?.remove();
                    }
                }
            }
        };
        let myPane = new CupertinoPane(".cupertino-pane", settings);
        pane = await myPane.present({ animate: true });
    });

    let type: "mini" | "info" | "reviews" = "mini";
</script>

<div class="cupertino-pane">
    <header>
        <CategoryChip category={place.category} />
        <PlaceHeader
            title={place.name}
            address1={place.address.line1}
            address2={place.address.line2}
        />
    </header>
    <Tabs bind:type />
    {#if type == "mini"}
        <Controls main_button="route" />
    {:else if type == "info"}
        <Description {place} />
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
        padding-bottom: 10px;
    }
</style>
