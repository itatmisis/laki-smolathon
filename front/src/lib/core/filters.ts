import type { IconKind } from "$lib";
import type { Category } from "./places";

export type Filter = {
    name: string;
    categories?: Category[];
    inside_city?: boolean;
}

export type FilterIcon = { title: string, icon: IconKind };

/** List of filters to display on the map screen. */
export const filter_list: FilterIcon[] = [
    { title: "Музеи", icon: "heart" },
    { title: "Храмы", icon: "heart" },
    { title: "Соборы", icon: "heart" },
    { title: "Памятники", icon: "heart" },
];
