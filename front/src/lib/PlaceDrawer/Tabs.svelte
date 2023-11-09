<script lang="ts">
    import Tab from "./Tab.svelte";

    export let type: "mini" | "info" | "reviews";

    function on_click(_type: typeof type) {
        if (type != _type) {
            type = _type;
        } else {
            type = "mini";
        }
    }
</script>

<div>
    <Tab text="Описание" selected={type == "info"} on:click={() => on_click("info")} />
    <Tab text="Реакции" num={6} selected={type == "reviews"} on:click={() => on_click("reviews")} />
</div>

<style lang="scss">
    div {
        display: flex;
        gap: 5px;
        margin: 10px 0;
    }
</style>
