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
    :root {
        --white1: #fcfcff;
        --white2: #f0f0fb;
        --black: #262634;
        --gray-system: #bfbfce;
        --gray-text: #8b8b8b;
        --system-gray-base: #eeeeee;
        --emphis1: #ee444f;
        --emphis2: #ff9a29;
        --emphis2-dark: #d48329;
        --emphis3: #f07f40;
        --emphis4: #dc4774;
        --success: #4ade25;
        --failure: #de2525;
    }

    :global(*) {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        font-family: "Roboto Slab", serif;
    }

    :global(.secondary-text) {
        font-size: 13px;
        color: #d9d9d9;
    }

    .wrapper {
        display: flex;
        flex-direction: column;
        justify-content: stretch;
        align-items: stretch;

        width: 100vw;
        height: 100dvh;
        background-color: var(--white2);
    }
</style>
