<script lang="ts">
    import type { Place } from "$lib/core/places";

    export let place: Place;
</script>

<div class="content">
    {#each place.description as entry}
        {#if entry.kind == "text"}
            <p>{entry.content}</p>
        {:else if entry.kind == "image"}
            <!-- svelte-ignore a11y-missing-attribute -->
            <img src={entry.content}/>
        {/if}
    {/each}
</div>

<style lang="scss">
    .content {
        display: flex;
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
        margin: 8px 0;
        p {
            font-size: 15px;
            text-indent: 10px;
        }
        img {
            border-radius: 8px;
        }
    }
</style>
