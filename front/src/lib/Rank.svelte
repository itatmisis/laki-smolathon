<script lang="ts">
    export let rank: Rank;

    type Rank =
        | "Смолодец"
        | "Смолодчинка"
        | "Смолодличинка";

    const rank_image: Record<Rank, string> = {
        "Смолодец": "icons/heart.svg",
        "Смолодчинка": "icons/heart.svg",
        "Смолодличинка": "icons/heart.svg"
    };
</script>

<span>
    <!-- svelte-ignore a11y-missing-attribute -->
    <img src={rank_image[rank]}/>
    <span>{rank}</span>
</span>

<style lang="scss">
    span {
        font-size: 14;
    }
    img {
        height: 16px;
        width: 16px;
    }
</style>
