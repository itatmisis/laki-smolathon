<script>
    import BottomBar from "../routes/BottomBar.svelte";
</script>

<div class="wrapper">
    <slot />
    <BottomBar />
</div>

<style lang="scss">
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
