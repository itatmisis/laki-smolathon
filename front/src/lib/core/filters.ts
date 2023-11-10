import type { Category } from "./places";

export type Filter = {
    name: string;
    categories?: Category[];
    inside_city?: boolean;
}
