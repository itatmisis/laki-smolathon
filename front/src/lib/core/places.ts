import { url, type IconKind } from "$lib";
import type { LngLat } from "@yandex/ymaps3-types";
import { secure_fetch } from "./auth";
import type { Filter } from "./filters";

export function getListOfPlaces(filter: Filter) {
    // TODO
}

export type Place = {
    id: number;
    id_category: number;
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
    "Музеи": { icon: "museum", color: "#DC4774" },
};

const Categories = ["Памятники", "История", "Церкви", "Музеи"] as const;

export async function PlacesList(): Promise<Place[]> {
    let response = await secure_fetch("map/location");
    let json: Array<any> = await response.json();
    let list: Array<Place> = [];
    for (const entry of json) {
        list.push(shit_to_place(entry));
    }
    return list;
}

export async function place(id: number): Promise<Place> {
    let response = await fetch(url(`map/location/${id}`));
    let json = await response.json();
    return shit_to_place(json);
}

let categories = {
    "1": { "name": "Памятники" },
    "2": { "name": "Церкви" },
    "3": { "name": "История" },
    "4": { "name": "Музеи" }
} as const;

function shit_to_place(shit: any): Place {
    return {
        id: shit.id,
        name: shit.name,
        address: {
            line1: shit.address,
            line2: ""
        },
        category: categories[shit.id_category as "1" | "2" | "3" | "4"].name as any, // TODO
        id_category: shit.id_category,
        description: [{ kind: "text", content: shit.description }],
        location: [shit.coord_x, shit.coord_y]
    };
}
