<script lang="ts">
    import type { IconKind } from "$lib";

    export let kind: IconKind | number;
</script>

<!-- svelte-ignore a11y-missing-attribute -->
<div class="marker">
    <img src={`icons/marker.svg`} />
    {#if typeof kind == "number"}
        <span>{kind}</span>
    {:else}
        <img class="icon" src={`icons/${kind}.svg`} />
    {/if}
</div>

<style lang="scss">
    .marker {
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;

        width: 32px;
        height: 32px;

        transform: translateY(
            -32px
        ); // TODO: the exact location of the marker on the map changes with zoom

        img {
            position: absolute;
        }
        span {
            display: block;
            color: white;
            z-index: 1;
            font-family: monospace;
            font-size: 15px;
            transform: translateY(-2px) translateX(1px);
        }
        .icon {
            width: 16px;
            height: 16px;
            filter: invert(1);
        }
    }
</style>
