<script lang="ts">
    import Icon from "$lib/Icon.svelte";

    export let text: string;
</script>

<button>
    {text}
    <Icon kind="forward"></Icon>
</button>

<style lang="scss">
    button {
        display: flex;
        align-items: center;
        justify-content: space-between;
        font-size: 15px;
        font-weight: bold;
        border-width: 0;
        background-color: transparent;
        --icon-size: 16px;
    }
</style>
