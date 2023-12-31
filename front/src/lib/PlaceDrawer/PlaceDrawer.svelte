<script lang="ts">
    import { CupertinoPane, type CupertinoSettings } from "cupertino-pane";
    import CategoryChip from "$lib/CategoryChip.svelte";
    import PlaceHeader from "$lib/PlaceHeader.svelte";
    import { onMount } from "svelte";
    import Description from "./Description.svelte";
    import Tabs from "./Tabs.svelte";
    import Controls from "./Controls.svelte";
    import Reviews from "./Reviews/Reviews.svelte";
    import { CategoriesIcons, type Place } from "$lib/core/places";

    export let place: Place;
    $: _category = CategoriesIcons[place.category];

    let pane: CupertinoPane;
    onMount(async () => {
        let settings: CupertinoSettings = {
            bottomClose: true,
            fitHeight: true,
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
        <CategoryChip title={place.category} color={_category.color} icon={_category.icon} small />
        <PlaceHeader
            title={place.name}
            address1={place.address.line1}
            address2={place.address.line2}
        />
    </header>
    <Tabs bind:type on:change={() => pane.calcFitHeight(false)} />
    {#if type == "mini"}
        <Controls id={place.id} main_button="route" />
    {:else if type == "info"}
        <Description {place} />
        <Controls id={place.id} main_button="route" />
    {:else if type == "reviews"}
        <Reviews id={place.id} />
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
        gap: 8px;

        align-items: start;
        margin: -20px;
        padding: 20px;
        margin-bottom: 0;
        padding-bottom: 10px;
    }
</style>
