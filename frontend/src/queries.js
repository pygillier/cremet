import { gql } from "apollo-boost";

export const ALL_CITIES = gql`
{
    allCities {
        edges {
            node {
                id
                name
                slug
            }
        }
    }
}`;