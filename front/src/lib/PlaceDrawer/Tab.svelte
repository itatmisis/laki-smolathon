<script lang="ts">
    export let text: string;
    export let num: number | undefined = undefined;
    export let selected: boolean = false;
</script>

<button on:click class:selected>
    {text}
    {#if num}
        <mark>{num}</mark>
    {/if}
</button>

<style lang="scss">
    button {
        display: flex;
        gap: 4px;
        align-items: center;
        background-color: white;
        border: 1px solid var(--black);
        border-radius: 8px;
        padding: 4px 6px;
        font-size: 13px;

        mark {
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--black);
            background-color: var(--gray-system);
            width: 16px;
            height: 16px;
            border-radius: 2px;
        }
        &.selected {
            color: var(--white1);
            background-color: var(--black);
            mark {
                background-color: var(--white2);
            }
        }
    }
</style>
