<script>
    import BottomBar from "./BottomBar.svelte";
</script>

<div class="wrapper">
    <slot />
    <BottomBar />
</div>

<svelte:head>
    <script
        src="https://api-maps.yandex.ru/v3/?apikey=4ec2de1f-586a-430a-a276-623e19416e79&lang=ru_RU"
    ></script>
</svelte:head>

<style lang="scss">
    :global(*) {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        font-family: 'Roboto Slab', sans-serif;
    }

    .wrapper {
        display: flex;
        flex-direction: column;
        justify-content: stretch;
        align-items: stretch;

        width: 100vw;
        height: 100vh;
    }
</style>
