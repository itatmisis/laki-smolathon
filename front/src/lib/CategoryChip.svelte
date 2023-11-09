<script lang="ts">
    import Icon from "./Icon.svelte";

    export let category: string;
</script>

<span class="chip">
    <Icon kind="heart" />
    <span>{category}</span>
</span>

<style lang="scss">
    .chip {
        display: flex;
        gap: 5px;
        align-items: center;
        --icon-invert: 1;
        --icon-size: 16px;
        color: white;
        background-color: #727272;
        border-radius: 8px;
        padding: 8px;
        margin-bottom: 12px;
    }
</style>
