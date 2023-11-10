import type { IconKind } from "$lib";
import type { LngLat } from "@yandex/ymaps3-types";
import type { Filter } from "./filters";

export function getListOfPlaces(filter: Filter) {
    // TODO
}

export type Place = {
    name: string;
    /** HTML */
    description: Description;
    category: Category;
    location: LngLat;
    address: {
        line1: string;
        line2: string;
    }
};

export type Description = { kind: "text" | "image", content: string }[];

export type Category = (typeof Categories)[number];

export type CategoryIcon = { icon: IconKind, color: string };

/** List of filters to display on the map screen. */
export const CategoriesIcons: Record<Category, CategoryIcon> = {
    "Памятники": { icon: "monument", color: "#FF9A29" },
    "История": { icon: "history", color: "#F07F40" },
    "Церкви": { icon: "church", color: "#EE444F" },
    "Музеи": { icon: "museum", color: "#FF9A29" },
};

const Categories = ["Памятники", "История", "Церкви", "Музеи"] as const;

export function PlacesList(): Record<number, Place> {
    return {
        0: { name: "", category: "Музеи", description: [], location: [32.050440, 54.779149], address: { line1: "", line2: "" } },
        1: { name: "", category: "Музеи", description: [], location: [32.039652, 54.784326], address: { line1: "", line2: "" } },
        // 2: { name: "", category: "Музеи", description: "", location: [32.038918, 54.783035], address: { line1: "", line2: "" } },
        // 3: { name: "", category: "Музеи", description: "", location: [32.038919, 54.783035], address: { line1: "", line2: "" } },
        // 4: { name: "", category: "Музеи", description: "", location: [32.043420, 54.773421], address: { line1: "", line2: "" } },
    };
}

export function place(id: number): Place {
    return {
        name: "Собор святой Богородицы",
        location: [0, 0],
        address: {
            line1: "ул. Клюшкина, д. 106",
            line2: "137568, Смоленская область, г. Смоленск",
        },
        description: [
            { kind: "text", content: "Основан Владимиром Мономахом, который положил начало каменному строительству на северо-востоке Руси." },
            { kind: "image", content: "https://www.pravmir.ru/wp-content/uploads/2018/11/2017_10_22-035_04-900x504.jpg" },
            { kind: "text", content: "3 июня 1611 года после 20-месячной осады польский король Сигизмунд III захватил город. Собор стал последним рубежом обороны смолян. По одной из версий, оставшиеся в живых защитники, поняв, что не смогут остановить врага, героически погибли, взорвав пороховой погреб под собором. Однако захватчики не стали разрушать собор. Они перекрыли его досками и устроили в нем костел." },
        ],
        category: "Церкви",
    };
}
