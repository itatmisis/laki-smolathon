<script lang="ts">
    import StatEntry from "./StatEntry.svelte";
</script>

<div>
    <p class="overall">
        Вы посетили <mark>88</mark> Смоленских мест<br />
        Заполнили дневник для <mark>12</mark> из них<br />
    </p>
    <div class="categories">
        <StatEntry category="Памятники" count={5} />
        <StatEntry category="История" count={5} />
        <StatEntry category="Церкви" count={5} />
        <StatEntry category="Музеи" count={5} />
    </div>
</div>

<style lang="scss">
    .overall {
        font-size: 15px;
        > mark {
            background-color: var(--white1);
            padding: 2px 8px;
            border-radius: 8px;
        }
        margin-bottom: 8px;
    }
    .categories {
        display: flex;
        flex-wrap: wrap;
        gap: 4px;
    }
</style>
