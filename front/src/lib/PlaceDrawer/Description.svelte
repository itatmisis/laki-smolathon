<script lang="ts">
    import type { Place } from "$lib/core/places";

    export let place: Place;
</script>

<div class="content">
    {#each place.description as entry}
        {#if entry.kind == "text"}
            <p>{entry.content}</p>
        {:else if entry.kind == "image"}
            <img src="https://www.pravmir.ru/wp-content/uploads/2018/11/2017_10_22-035_04-900x504.jpg"/>
        {/if}
    {/each}
</div>

<style lang="scss">
    .content {
        display: flex;
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
        margin: 20px;
        p {
            font-size: 15px;
            text-indent: 10px;
        }
        img {
            border-radius: 8px;
        }
    }
</style>
