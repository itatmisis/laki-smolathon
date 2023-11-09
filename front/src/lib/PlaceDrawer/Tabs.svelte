<script lang="ts">
    import Tab from "./Tab.svelte";

    export let tab: "Описание" | "Реакции" | undefined = undefined;
</script>

<div>
    <Tab text="Описание" selected={tab == "Описание"} on:click={()=>tab="Описание"} />
    <Tab text="Реакции" num={6} selected={tab == "Реакции"} on:click={()=>tab="Реакции"} />
</div>

<style lang="scss">
    div {
        display: flex;
        gap: 5px;
        margin: 10px 0;
    }
</style>
