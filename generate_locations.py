#!/usr/bin/env python3
"""
Generate location pages for Port Orange Concrete Co
Cities within 60-min drive of Port Orange, FL
"""
import os
import re

# Location data: (slug, city_name, county, existing)
LOCATIONS = [
    # Volusia County (home county)
    ("daytona-beach-shores", "Daytona Beach Shores", "Volusia", False),
    ("holly-hill", "Holly Hill", "Volusia", False),
    ("south-daytona", "South Daytona", "Volusia", False),
    ("edgewater", "Edgewater", "Volusia", False),
    ("oak-hill", "Oak Hill", "Volusia", False),
    ("orange-city", "Orange City", "Volusia", False),
    ("debary", "DeBary", "Volusia", False),
    ("lake-helen", "Lake Helen", "Volusia", False),
    ("pierson", "Pierson", "Volusia", False),
    ("ponce-inlet", "Ponce Inlet", "Volusia", False),
    ("ormond-by-the-sea", "Ormond-by-the-Sea", "Volusia", False),
    
    # Flagler County (north)
    ("palm-coast", "Palm Coast", "Flagler", False),
    ("bunnell", "Bunnell", "Flagler", False),
    ("beverly-beach", "Beverly Beach", "Flagler", False),
    
    # Brevard County (south)
    ("titusville", "Titusville", "Brevard", False),
    ("mims", "Mims", "Brevard", False),
    ("cape-canaveral", "Cape Canaveral", "Brevard", False),
    ("cocoa", "Cocoa", "Brevard", False),
    ("cocoa-beach", "Cocoa Beach", "Brevard", False),
    ("rockledge", "Rockledge", "Brevard", False),
    
    # Seminole County (west)
    ("sanford", "Sanford", "Seminole", False),
    ("lake-mary", "Lake Mary", "Seminole", False),
    ("longwood", "Longwood", "Seminole", False),
    ("altamonte-springs", "Altamonte Springs", "Seminole", False),
    ("casselberry", "Casselberry", "Seminole", False),
    ("winter-springs", "Winter Springs", "Seminole", False),
    ("oviedo", "Oviedo", "Seminole", False),
]

# Existing locations (already have pages)
EXISTING = {
    "concrete-contractors-daytona-beach": ("Daytona Beach", "Volusia"),
    "concrete-contractors-ormond-beach": ("Ormond Beach", "Volusia"),
    "concrete-contractors-new-smyrna-beach": ("New Smyrna Beach", "Volusia"),
    "concrete-contractors-deland": ("DeLand", "Volusia"),
    "concrete-contractors-deltona": ("Deltona", "Volusia"),
    "concrete-contractors-flagler-beach": ("Flagler Beach", "Flagler"),
}

TEMPLATE = '''<!DOCTYPE html>
<html lang="en-US" class="twbb">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Concrete Contractors {city}, FL | Driveways, Patios, Slabs</title>
<meta name="description" content="Looking for reliable concrete contractors in {city}, {county} County FL? Port Orange Concrete Co provides expert concrete services. Free estimates!"/>
<meta name="robots" content="follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large"/>
<link rel="canonical" href="https://concreteportorange.com/locations/{slug}/" />
<meta property="og:locale" content="en_US" />
<meta property="og:type" content="article" />
<meta property="og:title" content="Concrete Contractors {city}, FL | Driveways, Patios, Slabs" />
<meta property="og:description" content="Looking for reliable concrete contractors in {city}, {county} County FL? Port Orange Concrete Co provides expert concrete services. Free estimates!" />
<meta property="og:url" content="https://concreteportorange.com/locations/{slug}/" />
<meta property="og:site_name" content="Port Orange Concrete Co" />
<meta property="og:image" content="https://concreteportorange.com/wp-content/uploads/2023/11/concrete-driveway-scaled-1-1024x682.webp" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Concrete Contractors {city}, FL | Driveways, Patios, Slabs" />
<meta name="twitter:description" content="Looking for reliable concrete contractors in {city}, {county} County FL? Port Orange Concrete Co provides expert concrete services. Free estimates!" />
<link rel='stylesheet' id='elementor-frontend-css' href='/wp-content/plugins/elementor/assets/css/frontend.min.css@ver=3.34.2.css' type='text/css' media='all' />
<link rel='stylesheet' id='twbb-frontend-styles-css' href='/wp-content/plugins/tenweb-builder/assets/frontend/css/frontend.min.css@ver=1.37.61.css' type='text/css' media='all' />
<link rel='stylesheet' id='twbb-pro-features-css' href='/wp-content/plugins/tenweb-builder/pro-features/assets/css/frontend.min.css@ver=1.37.61.css' type='text/css' media='all' />
<link rel='stylesheet' id='widget-heading-css' href='/wp-content/plugins/elementor/assets/css/widget-heading.min.css@ver=3.34.2.css' type='text/css' media='all' />
<link rel='stylesheet' id='widget-icon-list-css' href='/wp-content/plugins/elementor/assets/css/widget-icon-list.min.css@ver=3.34.2.css' type='text/css' media='all' />
<link rel='stylesheet' id='widget-icon-box-css' href='/wp-content/plugins/elementor/assets/css/widget-icon-box.min.css@ver=3.34.2.css' type='text/css' media='all' />
<link rel='stylesheet' id='tenweb-website-builder-theme-style-css' href='/wp-content/themes/tenweb-website-builder-theme/assets/css/styles.min.css@ver=2.1.19.css' type='text/css' media='all' />
<link rel='stylesheet' id='elementor-gf-local-montserrat-css' href='/wp-content/uploads/elementor/google-fonts/css/montserrat.css@ver=1746149316.css' type='text/css' media='all' />
<link rel='stylesheet' id='elementor-icons-shared-0-css' href='/wp-content/plugins/elementor/assets/lib/font-awesome/css/fontawesome.min.css@ver=5.15.3.css' type='text/css' media='all' />
<link rel='stylesheet' id='elementor-icons-fa-solid-css' href='/wp-content/plugins/elementor/assets/lib/font-awesome/css/solid.min.css@ver=5.15.3.css' type='text/css' media='all' />
<link rel="icon" href="/wp-content/uploads/2023/10/cropped-Logo-Concrete-Co.-9-e1709071053354-32x32.png" sizes="32x32" />
<style>
html, body {{ max-width: 100%; overflow-x: hidden; }}
.location-hero {{ background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('/wp-content/uploads/2023/11/concrete-driveway-scaled-1-1024x682.webp'); background-size: cover; background-position: center; padding: 80px 20px; text-align: center; color: white; }}
.location-hero h1 {{ font-size: 2.5em; margin-bottom: 20px; font-family: 'Montserrat', sans-serif; }}
.location-hero p {{ font-size: 1.2em; max-width: 700px; margin: 0 auto 30px; }}
.cta-button {{ background: #f5a623; color: white; padding: 15px 30px; text-decoration: none; font-weight: bold; border-radius: 5px; display: inline-block; }}
.cta-button:hover {{ background: #e09000; }}
.content-section {{ max-width: 1200px; margin: 0 auto; padding: 60px 20px; }}
.services-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; margin: 40px 0; }}
.service-card {{ background: #f9f9f9; padding: 30px; border-radius: 10px; text-align: center; }}
.service-card i {{ font-size: 3em; color: #f5a623; margin-bottom: 20px; }}
.service-card h3 {{ margin-bottom: 15px; font-family: 'Montserrat', sans-serif; }}
.areas-section {{ background: #f5f5f5; padding: 60px 20px; }}
.areas-list {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; margin-top: 30px; }}
.areas-list a {{ background: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; color: #333; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
.areas-list a:hover {{ background: #f5a623; color: white; }}
footer {{ background: #333; color: white; padding: 40px 20px; text-align: center; }}
footer a {{ color: #f5a623; text-decoration: none; }}
.phone-link {{ color: #f5a623; font-size: 1.3em; font-weight: bold; }}
</style>
</head>
<body>
<!-- Header -->
<header style="background: #222; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
    <a href="/"><img src="/wp-content/uploads/2024/03/4-e1711057820476.png" alt="Port Orange Concrete Co" style="height: 50px;"></a>
    <nav style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
        <a href="/" style="color: white; text-decoration: none;">Home</a>
        <a href="/about/" style="color: white; text-decoration: none;">About</a>
        <a href="/locations/" style="color: white; text-decoration: none;">Service Areas</a>
        <a href="/contact/" style="color: white; text-decoration: none;">Contact</a>
        <a href="tel:+13862208770" class="cta-button">Call (386) 220-8770</a>
    </nav>
</header>

<!-- Hero Section -->
<section class="location-hero">
    <h1>Concrete Contractors in {city}, FL</h1>
    <p>Serving {city} and all of {county} County with professional concrete services. Driveways, patios, sidewalks, slabs, and more.</p>
    <a href="tel:+13862208770" class="cta-button">Get Your Free Estimate</a>
</section>

<!-- Main Content -->
<section class="content-section">
    <h2 style="text-align: center; font-family: 'Montserrat', sans-serif;">Professional Concrete Services in {city}</h2>
    <p style="text-align: center; max-width: 800px; margin: 20px auto;">
        Port Orange Concrete Co is proud to serve {city} and the surrounding {county} County area. Our experienced team delivers high-quality concrete work for residential and commercial properties.
    </p>
    
    <div class="services-grid">
        <div class="service-card">
            <i class="fas fa-road"></i>
            <h3>Concrete Driveways</h3>
            <p>Durable, beautiful driveways built to last. We offer standard, stamped, and decorative concrete options.</p>
        </div>
        <div class="service-card">
            <i class="fas fa-umbrella-beach"></i>
            <h3>Concrete Patios</h3>
            <p>Transform your outdoor living space with a custom concrete patio perfect for Florida weather.</p>
        </div>
        <div class="service-card">
            <i class="fas fa-cube"></i>
            <h3>Concrete Slabs</h3>
            <p>From garage floors to shed foundations, we pour reliable concrete slabs for any project.</p>
        </div>
        <div class="service-card">
            <i class="fas fa-walking"></i>
            <h3>Sidewalks & Walkways</h3>
            <p>Safe, attractive sidewalks and walkways that enhance your property's curb appeal.</p>
        </div>
        <div class="service-card">
            <i class="fas fa-home"></i>
            <h3>Foundations</h3>
            <p>Strong concrete foundations for new construction and additions to existing structures.</p>
        </div>
        <div class="service-card">
            <i class="fas fa-swimming-pool"></i>
            <h3>Pool Decks</h3>
            <p>Non-slip, cool-to-touch pool deck surfaces perfect for Florida's hot climate.</p>
        </div>
    </div>
    
    <div style="text-align: center; margin-top: 40px;">
        <h3>Ready to Start Your Project in {city}?</h3>
        <p>Call us today for a free, no-obligation estimate.</p>
        <a href="tel:+13862208770" class="phone-link">(386) 220-8770</a>
    </div>
</section>

<!-- Service Areas -->
<section class="areas-section">
    <div style="max-width: 1200px; margin: 0 auto; text-align: center;">
        <h2 style="font-family: 'Montserrat', sans-serif;">Other Areas We Serve</h2>
        <p>In addition to {city}, we provide concrete services throughout Central Florida:</p>
        <div class="areas-list">
            <a href="/concrete-contractors-daytona-beach/">Daytona Beach</a>
            <a href="/concrete-contractors-ormond-beach/">Ormond Beach</a>
            <a href="/concrete-contractors-new-smyrna-beach/">New Smyrna Beach</a>
            <a href="/concrete-contractors-deland/">DeLand</a>
            <a href="/concrete-contractors-deltona/">Deltona</a>
            <a href="/concrete-contractors-flagler-beach/">Flagler Beach</a>
            <a href="/locations/">View All Locations</a>
        </div>
    </div>
</section>

<!-- Footer -->
<footer>
    <div style="max-width: 1200px; margin: 0 auto;">
        <p style="font-size: 1.2em; margin-bottom: 20px;">Port Orange Concrete Co</p>
        <p>3742 S Nova Rd, Port Orange, FL 32129</p>
        <p><a href="tel:+13862208770">(386) 220-8770</a> | <a href="mailto:info@concreteportorange.com">info@concreteportorange.com</a></p>
        <nav style="margin: 30px 0;">
            <a href="/" style="margin: 0 15px;">Home</a>
            <a href="/about/" style="margin: 0 15px;">About</a>
            <a href="/locations/" style="margin: 0 15px;">Service Areas</a>
            <a href="/contact/" style="margin: 0 15px;">Contact</a>
        </nav>
        <p style="color: #888; font-size: 0.9em;">&copy; 2024 Port Orange Concrete Co. All rights reserved.</p>
    </div>
</footer>
</body>
</html>
'''

def generate_locations():
    """Generate all location pages"""
    os.makedirs('locations', exist_ok=True)
    
    count = 0
    for slug, city, county, _ in LOCATIONS:
        dir_path = f'locations/{slug}'
        os.makedirs(dir_path, exist_ok=True)
        
        html = TEMPLATE.format(
            city=city,
            county=county,
            slug=slug
        )
        
        with open(f'{dir_path}/index.html', 'w') as f:
            f.write(html)
        
        print(f'Created: locations/{slug}/index.html')
        count += 1
    
    print(f'\nTotal new location pages created: {count}')
    return count

def generate_locations_index():
    """Generate the /locations/ index page"""
    
    # Group locations by county
    counties = {
        'Volusia': [],
        'Flagler': [],
        'Brevard': [],
        'Seminole': []
    }
    
    # Add existing locations
    for slug, (city, county) in EXISTING.items():
        counties[county].append((slug, city, True))
    
    # Add new locations
    for slug, city, county, _ in LOCATIONS:
        counties[county].append((f'locations/{slug}', city, False))
    
    # Sort each county alphabetically
    for county in counties:
        counties[county].sort(key=lambda x: x[1])
    
    html = '''<!DOCTYPE html>
<html lang="en-US" class="twbb">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Service Areas | Port Orange Concrete Co</title>
<meta name="description" content="Port Orange Concrete Co serves all of Central Florida. View our complete list of service areas including Volusia, Flagler, Brevard, and Seminole counties."/>
<meta name="robots" content="follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large"/>
<link rel="canonical" href="https://concreteportorange.com/locations/" />
<meta property="og:locale" content="en_US" />
<meta property="og:type" content="article" />
<meta property="og:title" content="Service Areas | Port Orange Concrete Co" />
<meta property="og:description" content="Port Orange Concrete Co serves all of Central Florida. View our complete list of service areas." />
<meta property="og:url" content="https://concreteportorange.com/locations/" />
<meta property="og:site_name" content="Port Orange Concrete Co" />
<link rel='stylesheet' href='/wp-content/plugins/elementor/assets/css/frontend.min.css@ver=3.34.2.css' type='text/css' />
<link rel='stylesheet' href='/wp-content/plugins/tenweb-builder/assets/frontend/css/frontend.min.css@ver=1.37.61.css' type='text/css' />
<link rel='stylesheet' href='/wp-content/plugins/tenweb-builder/pro-features/assets/css/frontend.min.css@ver=1.37.61.css' type='text/css' />
<link rel='stylesheet' href='/wp-content/themes/tenweb-website-builder-theme/assets/css/styles.min.css@ver=2.1.19.css' type='text/css' />
<link rel='stylesheet' href='/wp-content/uploads/elementor/google-fonts/css/montserrat.css@ver=1746149316.css' type='text/css' />
<link rel='stylesheet' href='/wp-content/plugins/elementor/assets/lib/font-awesome/css/fontawesome.min.css@ver=5.15.3.css' type='text/css' />
<link rel='stylesheet' href='/wp-content/plugins/elementor/assets/lib/font-awesome/css/solid.min.css@ver=5.15.3.css' type='text/css' />
<link rel="icon" href="/wp-content/uploads/2023/10/cropped-Logo-Concrete-Co.-9-e1709071053354-32x32.png" sizes="32x32" />
<style>
html, body { max-width: 100%; overflow-x: hidden; }
.page-hero { background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('/wp-content/uploads/2023/11/concrete-driveway-scaled-1-1024x682.webp'); background-size: cover; background-position: center; padding: 80px 20px; text-align: center; color: white; }
.page-hero h1 { font-size: 2.5em; margin-bottom: 20px; font-family: 'Montserrat', sans-serif; }
.page-hero p { font-size: 1.2em; max-width: 700px; margin: 0 auto; }
.content-section { max-width: 1200px; margin: 0 auto; padding: 60px 20px; }
.county-section { margin-bottom: 50px; }
.county-section h2 { font-family: 'Montserrat', sans-serif; color: #333; border-bottom: 3px solid #f5a623; padding-bottom: 10px; margin-bottom: 20px; }
.locations-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px; }
.location-link { background: #f9f9f9; padding: 15px 20px; border-radius: 5px; text-decoration: none; color: #333; display: block; transition: all 0.3s; }
.location-link:hover { background: #f5a623; color: white; transform: translateY(-2px); }
.cta-button { background: #f5a623; color: white; padding: 15px 30px; text-decoration: none; font-weight: bold; border-radius: 5px; display: inline-block; }
footer { background: #333; color: white; padding: 40px 20px; text-align: center; }
footer a { color: #f5a623; text-decoration: none; }
</style>
</head>
<body>
<!-- Header -->
<header style="background: #222; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
    <a href="/"><img src="/wp-content/uploads/2024/03/4-e1711057820476.png" alt="Port Orange Concrete Co" style="height: 50px;"></a>
    <nav style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
        <a href="/" style="color: white; text-decoration: none;">Home</a>
        <a href="/about/" style="color: white; text-decoration: none;">About</a>
        <a href="/locations/" style="color: #f5a623; text-decoration: none; font-weight: bold;">Service Areas</a>
        <a href="/contact/" style="color: white; text-decoration: none;">Contact</a>
        <a href="tel:+13862208770" class="cta-button">Call (386) 220-8770</a>
    </nav>
</header>

<!-- Hero Section -->
<section class="page-hero">
    <h1>Service Areas</h1>
    <p>Port Orange Concrete Co proudly serves communities throughout Central Florida. Find your city below!</p>
</section>

<!-- Main Content -->
<section class="content-section">
'''
    
    for county_name in ['Volusia', 'Flagler', 'Brevard', 'Seminole']:
        locations = counties[county_name]
        if locations:
            html += f'''
    <div class="county-section">
        <h2>{county_name} County</h2>
        <div class="locations-grid">
'''
            for slug, city, is_existing in locations:
                href = f'/{slug}/' if is_existing else f'/{slug}/'
                html += f'            <a href="{href}" class="location-link">{city}</a>\n'
            html += '''        </div>
    </div>
'''
    
    html += '''
    <div style="text-align: center; margin-top: 50px; padding: 40px; background: #f5f5f5; border-radius: 10px;">
        <h3 style="font-family: 'Montserrat', sans-serif;">Don't See Your City?</h3>
        <p>We may still be able to serve your area! Give us a call to discuss your project.</p>
        <a href="tel:+13862208770" class="cta-button" style="margin-top: 20px;">Call (386) 220-8770</a>
    </div>
</section>

<!-- Footer -->
<footer>
    <div style="max-width: 1200px; margin: 0 auto;">
        <p style="font-size: 1.2em; margin-bottom: 20px;">Port Orange Concrete Co</p>
        <p>3742 S Nova Rd, Port Orange, FL 32129</p>
        <p><a href="tel:+13862208770">(386) 220-8770</a> | <a href="mailto:info@concreteportorange.com">info@concreteportorange.com</a></p>
        <nav style="margin: 30px 0;">
            <a href="/" style="margin: 0 15px;">Home</a>
            <a href="/about/" style="margin: 0 15px;">About</a>
            <a href="/locations/" style="margin: 0 15px;">Service Areas</a>
            <a href="/contact/" style="margin: 0 15px;">Contact</a>
        </nav>
        <p style="color: #888; font-size: 0.9em;">&copy; 2024 Port Orange Concrete Co. All rights reserved.</p>
    </div>
</footer>
</body>
</html>
'''
    
    with open('locations/index.html', 'w') as f:
        f.write(html)
    
    print('Created: locations/index.html')

if __name__ == '__main__':
    os.chdir('/home/ec2-user/clawd/sites/portorange-concrete')
    new_count = generate_locations()
    generate_locations_index()
    print(f'\n✅ Generated {new_count} new location pages + 1 index page')
    print(f'📍 Total locations (including existing): {new_count + len(EXISTING)}')
