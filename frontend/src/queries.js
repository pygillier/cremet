import { gql } from "apollo-boost";

export const CITY_LIST_QUERY = gql`
{
    allCities {
        edges {
            node {
                id
                name
                slug
                venuesCount
            }
        }
    }
}`;

export const CITY_DETAIL_QUERY = gql`
query CityDetail($slug:String!) {
    allCities(slug:$slug) {
        edges {
            node {
                id
                name
                venuesCount
                venues {
                    edges {
                        node {
                            id
                            name
                            venueType
                            venueLabel
                        }
                    }
                }
            }
        }
    }
}
`;