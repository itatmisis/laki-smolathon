<script lang="ts">
    import type { TransitionConfig } from "svelte/transition";
    import { cubicOut } from "svelte/easing";

    type Mode = "tourist" | "explorer";

    export let selected: Mode = "explorer";

    function swap() {
        if (selected == "explorer") {
            selected = "tourist";
        } else {
            selected = "explorer";
        }
    }

    // function transition(node: HTMLElement, options: TransitionConfig) {
    //     return {
    //         duration: options.duration,
    //         easing: cubicOut,
    //         css: (t: number) => `
    //             transform:scaleX(${t}); transform-origin: top center;
    //         `
    //     };
    // }
</script>

<menu>
    {#if selected == "tourist"}
        <button on:click={swap}>
            <img src="svg/tourist-mode.svg" alt="Режим туриста" />
        </button>
    {:else}
        <button on:click={swap}>
            <img src="svg/explorer-mode.svg" alt="Режим приключенца" />
        </button>
    {/if}
</menu>

<style lang="scss">
    menu {
        display: flex;
        position: absolute;
        width: 100%;
        justify-content: center;
        height: 32px;

        top: var(--gap);

        button {
            position: absolute;
            background-color: transparent;
            border: 0;
        }
    }
</style>
