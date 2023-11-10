<script lang="ts">
    import type { Review as ReviewType } from "$lib";
    import Review from "./Review.svelte";

    let photos: Promise<string> = Promise.reject();

    let _reviews: ReviewType[] = [
        { name: "Иван Иванов", text: "Lorem impsum", photo: "icons/heart.svg", posted_at: "2022.02.02" },
        { name: "Рома Романов", text: "Lorem impsum", photo: "icons/heart.svg", posted_at: "2022.02.02" }
    ];
    let reviews: Promise<ReviewType[]> = Promise.resolve(_reviews);
</script>

<section>
    <div class="photos">
        {#await photos}
            Loading...
        {:then photos}
            {#each photos as photo}
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
