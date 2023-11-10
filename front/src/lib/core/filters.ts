import type { IconKind } from "$lib";
import type { Category } from "./places";

export type Filter = {
    name: string;
    categories?: Category[];
    inside_city?: boolean;
}

export type FilterIcon = { title: string, icon: IconKind, color: string };

/** List of filters to display on the map screen. */
export const filter_list: FilterIcon[] = [
    { title: "Памятники", icon: "monument", color: "#FF9A29" },
    { title: "История", icon: "history", color: "#F07F40" },
    { title: "Церкви", icon: "church", color: "#EE444F" },
    { title: "Музеи", icon: "museum", color: "#FF9A29" },
];
