<script lang="ts">
    import type { IconKind } from "$lib";

    export let kind: IconKind;
</script>

<!-- svelte-ignore a11y-missing-attribute -->
<img src={`/icons/${kind}.svg`} />

<style lang="scss">
    img {
        filter: invert(var(--icon-invert, 0));
        height: var(--icon-size, 32px);
        width: var(--icon-size, 32px);
    }
</style>
