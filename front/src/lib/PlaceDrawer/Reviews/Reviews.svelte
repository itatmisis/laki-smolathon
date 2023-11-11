<script lang="ts">
    import { journal_by_location, type JournalEntry } from "$lib/core/journal";
    import Controls from "../Controls.svelte";
    import Review from "./Review.svelte";

    export let id: number;

    let photos: Promise<string> = Promise.reject();
    let reviews: Promise<JournalEntry[]> = journal_by_location(id);

    let writing_self: boolean = false;
</script>

<section>
    <div class="photos">
        {#await photos}
            Loading...
        {:then photos}
            {#each photos as photo}
                <!-- svelte-ignore a11y-missing-attribute -->
                <img src={photo}/>
            {/each}
        {/await}
    </div>
    <section class="reviews">
        {#await reviews}
            Loading...
        {:then reviews}
            {#each reviews as review}
                <Review {review}/>
            {/each}
        {/await}
    </section>
    <Controls {id} main_button="review" />
</section>

<style lang="scss">
    .photos {
        width: 80px;
        height: 80px;
    }
    .reviews {
        display: flex;
        flex-direction: column;
        gap: 20px;
        margin-bottom: 20px;
    }
</style>
