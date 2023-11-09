import type { IconKind } from "$lib";

export type Filter = { title: string, icon: IconKind };

export const filter_list: Filter[] = [
    { title: "Музеи", icon: "heart" },
    { title: "Храмы", icon: "heart" },
    { title: "Соборы", icon: "heart" },
    { title: "Памятники", icon: "heart" },
];
