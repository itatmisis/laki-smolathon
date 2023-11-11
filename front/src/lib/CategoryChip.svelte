<script lang="ts">
    import type { IconKind } from "$lib";
    import Icon from "./Icon.svelte";

    export let title: string;
    export let icon: IconKind;
    export let color: string;

    export let small: boolean = false;
</script>

<button style:background-color={color} class:small>
    <Icon kind={icon} />
    <span>{title}</span>
</button>

<style lang="scss">
    button {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 4px;

        border-radius: 8px;
        border: 0;

        span {
            color: var(--white1);
            font-size: 13px;
        }

        --icon-size: 20px;
        padding: 8px 12px;
        &.small {
            --icon-size: 16px;
            padding: 8px 4px;
        }
    }
</style>
