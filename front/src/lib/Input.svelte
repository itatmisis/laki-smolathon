<script lang="ts">
    import type { HTMLInputTypeAttribute } from "svelte/elements";

    export let label: string;
    export let placeholder: string = "";
    export let type: "text" | "password" = "text";

    export let value: string;
</script>

<label>
    <span>{label}</span>
    {#if type == "text"}
        <input bind:value {placeholder} type="text" />
    {:else}
        <input bind:value {placeholder} type="password" />
    {/if}
</label>

<style lang="scss">
    label {
        display: flex;
        flex-direction: column;
        span {
            color: var(--gray-text);
            font-size: 13px;
        }
        input {
            height: 56px;
            font-size: 15px;
            border: 1px solid var(--gray-system);
            border-radius: 8px;
            padding: 20px 16px;
            background-color: var(--white1);
            outline: none;
            &:focus {
                border: 1px solid var(--black);
            }
        }
    }
</style>
