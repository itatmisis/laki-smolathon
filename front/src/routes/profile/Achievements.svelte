<script lang="ts">
    type Achievement = { name: string; image: string, foreground: string; background: string; };

    const achievements: Achievement[] = [
        { name: "Религиозный культивист", image: "religion", foreground: "white", background: "#EE444F" },
        { name: "Религиозный культивист", image: "monument", foreground: "black", background: "#FFFFFF" },
        { name: "Религиозный культивист", image: "history", foreground: "black", background: "#FFFFFF" },
        { name: "Религиозный культивист", image: "museum", foreground: "white", background: "#EE444F" },
    ];
</script>

<section>
    {#each achievements as achievement}
        <article
            style:color={achievement.foreground}
            style:background-color={achievement.background}
        >
            <img src={`achievements/${achievement.image}.svg`}/>
            <span>{achievement.name}</span>
        </article>
    {/each}
</section>

<style lang="scss">
    section {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-auto-rows: 160px;
        gap: 8px;
        align-items: stretch;
        article {
            display: flex;
            flex-direction: column;
            justify-content: start;
            align-items: center;
            border-radius: 8px;
            padding: 12px;
            padding-bottom: 4px;
            font-size: 15px;
            img {
                width: 100%;
            }
            span {
                text-align: center;
            }
        }
    }
</style>
