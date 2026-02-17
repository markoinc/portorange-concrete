export const site = {
  name: "Port Orange Concrete Co.",
  shortName: "Port Orange Concrete",
  tagline: "Volusia County's Trusted Concrete Experts",
  title: "Concrete Contractors Port Orange FL | Driveways, Patios, Slabs | Free Estimates",
  description: "Port Orange's #1 rated concrete contractors. Expert driveways, patios, slabs & stamped concrete. Licensed, insured, 20+ years experience. Call (386) 220-8770 for your FREE estimate!",
  phone: "(386) 220-8770",
  phoneLink: "tel:+13862208770",
  email: "info@concreteportorange.com",
  address: {
    street: "3742 S Nova Rd",
    city: "Port Orange",
    state: "FL",
    zip: "32129",
    full: "3742 S Nova Rd, Port Orange, FL 32129"
  },
  geo: {
    lat: 29.1086,
    lng: -81.0134
  },
  url: "https://concreteportorange.com",
  hours: {
    display: "Mon-Fri 7AM-6PM, Sat 8AM-4PM",
    schema: ["Mo-Fr 07:00-18:00", "Sa 08:00-16:00"]
  },
  // All cities within ~1 hour of Port Orange
  serviceAreas: [
    "Port Orange",
    "Daytona Beach",
    "Ormond Beach",
    "New Smyrna Beach",
    "DeLand",
    "Deltona",
    "Edgewater",
    "Holly Hill",
    "South Daytona",
    "Ponce Inlet",
    "Palm Coast",
    "Flagler Beach",
    "Orange City",
    "Lake Helen",
    "DeBary",
    "Sanford",
    "Lake Mary",
    "Titusville",
    "Oak Hill",
    "Volusia County"
  ],
  services: [
    { 
      name: "Concrete Driveways", 
      slug: "concrete-driveway-contractors", 
      description: "New driveways, extensions, repairs, and resurfacing for Port Orange homes",
      priceRange: "$8-$18/sq ft"
    },
    { 
      name: "Concrete Patios", 
      slug: "concrete-patio-contractors", 
      description: "Custom patios and outdoor living spaces designed for Florida weather",
      priceRange: "$10-$25/sq ft" 
    },
    { 
      name: "Concrete Slabs", 
      slug: "concrete-slab-contractors", 
      description: "Foundations, garage floors, shed pads, and equipment slabs",
      priceRange: "$6-$12/sq ft"
    },
    { 
      name: "Stamped Concrete", 
      slug: "stamped-concrete-contractors", 
      description: "Decorative patterns that mimic brick, stone, tile, and wood",
      priceRange: "$12-$25/sq ft"
    },
    { 
      name: "Concrete Repair", 
      slug: "concrete-repair-contractors", 
      description: "Crack repair, leveling, resurfacing, and restoration",
      priceRange: "$3-$8/sq ft"
    }
  ],
  socialLinks: {
    google: "https://maps.google.com/?q=Port+Orange+Concrete+Co"
  },
  stats: {
    yearsExperience: "20+",
    projectsCompleted: "1,500+",
    rating: "5.0",
    reviewCount: "127"
  }
};

export const reviews = [
  {
    name: "Michael R.",
    location: "Port Orange",
    rating: 5,
    text: "Outstanding work on our new driveway. The crew was professional, showed up on time, and the finished product looks amazing. Best concrete contractors in Port Orange! They even finished a day early.",
    date: "2025-01-15",
    color: "#0d9488",
    service: "Driveway"
  },
  {
    name: "Jennifer S.",
    location: "Daytona Beach",
    rating: 5,
    text: "We had a stamped patio installed and couldn't be happier. Fair pricing, excellent communication, and beautiful craftsmanship. The pattern looks exactly like natural stone. Highly recommend!",
    date: "2025-01-08",
    color: "#f97316",
    service: "Stamped Patio"
  },
  {
    name: "David L.",
    location: "Ormond Beach",
    rating: 5,
    text: "After getting several quotes, Port Orange Concrete offered the best value. They poured a new garage slab that's perfectly level. True professionals who know Florida soil conditions.",
    date: "2024-12-20",
    color: "#22c55e",
    service: "Garage Slab"
  },
  {
    name: "Sarah M.",
    location: "New Smyrna Beach",
    rating: 5,
    text: "Great experience from start to finish. They replaced our cracked sidewalk and it looks brand new. Clean job site and friendly crew. Would definitely use them again.",
    date: "2024-12-10",
    color: "#8b5cf6",
    service: "Sidewalk"
  },
  {
    name: "Robert K.",
    location: "DeLand",
    rating: 5,
    text: "Port Orange Concrete did an amazing job on our pool deck. Finished ahead of schedule and the quality is top-notch. They worked around our busy schedule perfectly.",
    date: "2024-11-28",
    color: "#ec4899",
    service: "Pool Deck"
  },
  {
    name: "Lisa T.",
    location: "Deltona",
    rating: 5,
    text: "Excellent work ethic and attention to detail. Our new patio turned out better than we imagined. The colored concrete matches our house perfectly. Very happy!",
    date: "2024-11-15",
    color: "#3b82f6",
    service: "Patio"
  },
  {
    name: "James H.",
    location: "Holly Hill",
    rating: 5,
    text: "Fast, professional, and affordable. They poured a shed foundation for us in one day. The base prep was thorough and the slab is perfectly level. A+ work.",
    date: "2024-11-01",
    color: "#14b8a6",
    service: "Shed Slab"
  },
  {
    name: "Patricia W.",
    location: "South Daytona",
    rating: 5,
    text: "We've used Port Orange Concrete twice now - first for our driveway, now for a patio extension. Consistent quality every time. They're our go-to concrete guys.",
    date: "2024-10-20",
    color: "#f59e0b",
    service: "Patio Extension"
  }
];

// All location pages - cities within 1 hour drive
export const locations = [
  { 
    name: "Daytona Beach", 
    slug: "concrete-contractors-daytona-beach",
    county: "Volusia County",
    distance: "10 minutes",
    population: "72,000+",
    description: "Home of the Daytona International Speedway"
  },
  { 
    name: "Ormond Beach", 
    slug: "concrete-contractors-ormond-beach",
    county: "Volusia County",
    distance: "15 minutes",
    population: "45,000+",
    description: "The Birthplace of Speed"
  },
  { 
    name: "New Smyrna Beach", 
    slug: "concrete-contractors-new-smyrna-beach",
    county: "Volusia County",
    distance: "12 minutes",
    population: "32,000+",
    description: "Historic beach town on the Indian River"
  },
  { 
    name: "DeLand", 
    slug: "concrete-contractors-deland",
    county: "Volusia County",
    distance: "25 minutes",
    population: "40,000+",
    description: "County seat of Volusia County"
  },
  { 
    name: "Deltona", 
    slug: "concrete-contractors-deltona",
    county: "Volusia County",
    distance: "30 minutes",
    population: "95,000+",
    description: "Largest city in Volusia County"
  },
  { 
    name: "Edgewater", 
    slug: "concrete-contractors-edgewater",
    county: "Volusia County",
    distance: "8 minutes",
    population: "27,000+",
    description: "Waterfront community on Mosquito Lagoon"
  },
  { 
    name: "Holly Hill", 
    slug: "concrete-contractors-holly-hill",
    county: "Volusia County",
    distance: "12 minutes",
    population: "13,000+",
    description: "Historic community near Daytona"
  },
  { 
    name: "South Daytona", 
    slug: "concrete-contractors-south-daytona",
    county: "Volusia County",
    distance: "5 minutes",
    population: "14,000+",
    description: "Adjacent to Port Orange on the Halifax River"
  },
  { 
    name: "Ponce Inlet", 
    slug: "concrete-contractors-ponce-inlet",
    county: "Volusia County",
    distance: "10 minutes",
    population: "3,500+",
    description: "Home of the historic Ponce de Leon Inlet Lighthouse"
  },
  { 
    name: "Palm Coast", 
    slug: "concrete-contractors-palm-coast",
    county: "Flagler County",
    distance: "35 minutes",
    population: "95,000+",
    description: "Fast-growing Flagler County city"
  },
  { 
    name: "Flagler Beach", 
    slug: "concrete-contractors-flagler-beach",
    county: "Flagler County",
    distance: "30 minutes",
    population: "5,500+",
    description: "Charming oceanfront community"
  },
  { 
    name: "Orange City", 
    slug: "concrete-contractors-orange-city",
    county: "Volusia County",
    distance: "25 minutes",
    population: "13,000+",
    description: "Near Blue Spring State Park"
  },
  { 
    name: "Lake Helen", 
    slug: "concrete-contractors-lake-helen",
    county: "Volusia County",
    distance: "20 minutes",
    population: "3,000+",
    description: "Quaint town near Cassadaga"
  },
  { 
    name: "DeBary", 
    slug: "concrete-contractors-debary",
    county: "Volusia County",
    distance: "35 minutes",
    population: "24,000+",
    description: "Gateway to the St. Johns River"
  },
  { 
    name: "Sanford", 
    slug: "concrete-contractors-sanford",
    county: "Seminole County",
    distance: "45 minutes",
    population: "63,000+",
    description: "Historic downtown on Lake Monroe"
  },
  { 
    name: "Lake Mary", 
    slug: "concrete-contractors-lake-mary",
    county: "Seminole County",
    distance: "50 minutes",
    population: "18,000+",
    description: "Affluent suburban community"
  },
  { 
    name: "Titusville", 
    slug: "concrete-contractors-titusville",
    county: "Brevard County",
    distance: "50 minutes",
    population: "50,000+",
    description: "Space Coast gateway to Kennedy Space Center"
  },
  { 
    name: "Oak Hill", 
    slug: "concrete-contractors-oak-hill",
    county: "Volusia County",
    distance: "15 minutes",
    population: "2,000+",
    description: "Quiet fishing community"
  }
];
