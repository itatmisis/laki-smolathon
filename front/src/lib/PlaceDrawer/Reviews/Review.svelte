<script lang="ts">
    import type { Review } from "$lib";
    import Rank from "$lib/Rank.svelte";

    export let review: Review;
</script>

<article>
    <!-- svelte-ignore a11y-missing-attribute -->
    <header>
        <img src={review.photo} />
        <div class="rows">
            <div class="first-row">
                <span>{review.name}</span>
                <span>{review.posted_at}</span>
            </div>
            <Rank rank="Смолодец" />
        </div>
    </header>
    <span class="text">{review.text}</span>
</article>

<style lang="scss">
    article {
        display: flex;
        flex-direction: column;
        align-items: stretch;
        background-color: grey;

        header {
            display: flex;
            .rows {
                display: flex;
                flex-direction: column;
                img {
                    height: 40px;
                    width: 40px;
                }
                .first-row {
                    flex: 1;
                    display: flex;
                    justify-content: space-between;
                }
            }
        }
        .text {
            
        }
    }
</style>
