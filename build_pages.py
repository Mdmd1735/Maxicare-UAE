"""Generate all MaxiCare service pages."""
import os, sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', errors='replace')

BRAND = '#1a3c5e'
ACCENT = '#d97706'

SERVICES = [
    {
        'slug': 'ac-services',
        'name': 'AC Services & Maintenance',
        'icon': 'fa-wind',
        'cat': 'Climate Control',
        'tagline': 'Cool Comfort, All Year Round',
        'hero_txt': 'AC Services<br>&amp; Maintenance',
        'intro': 'MaxiCare\'s AC division delivers expert air conditioning installation, servicing, repair and annual maintenance contracts across Dubai, Abu Dhabi and Sharjah. From split units to centralised HVAC systems, our certified technicians keep you cool regardless of the UAE\'s extreme heat.',
        'badge': 'Certified AC technicians — all major brands serviced.',
        'features': [
            'Installation of split, cassette, ducted and centralised AC units',
            'Annual Maintenance Contracts (AMC) with scheduled visits',
            'Gas top-up, coil cleaning and filter replacement',
            'Fault diagnosis and emergency repair for all brands',
            'Duct cleaning and disinfection to improve air quality',
            'Energy efficiency assessments to reduce utility bills',
            'Commercial chiller and VRF/VRV system maintenance',
        ],
        'why': 'The UAE\'s harsh climate demands a fully functional AC system year-round. Our dedicated AC team ensures fast response times and long-lasting repairs — not just quick fixes.',
    },
    {
        'slug': 'plumbing',
        'name': 'Plumbing Services',
        'icon': 'fa-wrench',
        'cat': 'Water & Plumbing',
        'tagline': 'No Leak Too Big or Small',
        'hero_txt': 'Plumbing<br>Services',
        'intro': 'From burst pipes and blocked drains to complete bathroom and kitchen installations, MaxiCare\'s licensed plumbing team delivers fast, reliable solutions for homes and commercial properties across the UAE.',
        'badge': 'Licensed plumbers — emergency response available.',
        'features': [
            'Emergency leak detection and repair',
            'Drain unblocking and CCTV drain inspection',
            'Water heater installation, repair and replacement',
            'Bathroom and kitchen plumbing fit-outs',
            'Pipe relaying and re-routing',
            'Water pressure testing and regulation',
            'Sanitary ware supply and installation',
        ],
        'why': 'Plumbing problems don\'t wait for business hours. MaxiCare\'s team is available for emergency call-outs with same-day response across Dubai, Abu Dhabi and Sharjah.',
    },
    {
        'slug': 'electrical-services',
        'name': 'Electrical Services',
        'icon': 'fa-bolt',
        'cat': 'Technical',
        'tagline': 'Safe, Certified Electrical Work',
        'hero_txt': 'Electrical<br>Services',
        'intro': 'MaxiCare\'s licensed electricians handle everything from fault diagnosis and wiring to full electrical fit-outs for homes, offices and commercial premises. All work conforms to UAE electrical safety regulations.',
        'badge': 'UAE-licensed electricians — safety-first approach.',
        'features': [
            'Electrical fault finding and repair',
            'Full residential and commercial wiring',
            'Distribution board upgrades and RCD installation',
            'Lighting design, supply and installation (LED upgrades)',
            'Power socket and switch installation',
            'Earthing and bonding inspections',
            'Generator installation and maintenance',
        ],
        'why': 'Electrical safety in the UAE\'s extreme climate is non-negotiable. MaxiCare\'s certified electricians work to DEWA and ADDC standards — protecting your property and occupants.',
    },
    {
        'slug': 'cleaning-services',
        'name': 'Cleaning Services',
        'icon': 'fa-broom',
        'cat': 'Cleaning & Hygiene',
        'tagline': 'Spotless Spaces, Every Visit',
        'hero_txt': 'Cleaning<br>Services',
        'intro': 'MaxiCare offers professional cleaning for villas, apartments, offices, retail outlets and commercial facilities. Choose from one-off deep cleans, regular maintenance schedules or post-construction clean-ups.',
        'badge': 'Eco-friendly products available on request.',
        'features': [
            'Deep cleaning for move-in / move-out',
            'Regular residential and commercial cleaning contracts',
            'Post-construction and renovation cleaning',
            'High-pressure jet washing for outdoor areas',
            'Steam cleaning for carpets and upholstery',
            'Window cleaning for high-rise and standard buildings',
            'Eco-friendly, non-toxic cleaning products available',
        ],
        'why': 'A clean environment directly impacts health, productivity and first impressions. MaxiCare uses professional-grade equipment and trained staff to deliver consistently excellent results.',
    },
    {
        'slug': 'pest-management',
        'name': 'Pest Management',
        'icon': 'fa-bug',
        'cat': 'Cleaning & Hygiene',
        'tagline': 'Eliminate Pests. Protect Your Space.',
        'hero_txt': 'Pest<br>Management',
        'intro': 'MaxiCare\'s pest management division provides safe, effective treatment for all common UAE pests — including cockroaches, rodents, ants, termites, bedbugs and flying insects — in homes, restaurants, hotels and commercial properties.',
        'badge': 'Safe treatments — child and pet friendly options available.',
        'features': [
            'Cockroach, ant and fly treatment using approved insecticides',
            'Rodent control — trapping and exclusion systems',
            'Termite treatment and prevention',
            'Bedbug heat treatment and chemical control',
            'Preventive pest control contracts for ongoing protection',
            'Food-safe treatments for commercial kitchens and restaurants',
            'Post-treatment follow-up and guarantee',
        ],
        'why': 'The UAE\'s warm climate creates ideal breeding conditions for pests. MaxiCare\'s integrated pest management approach eliminates active infestations and prevents recurrence — protecting your health and reputation.',
    },
    {
        'slug': 'swimming-pool',
        'name': 'Swimming Pool Services',
        'icon': 'fa-swimmer',
        'cat': 'Water & Plumbing',
        'tagline': 'Crystal Clear Pools, Year Round',
        'hero_txt': 'Swimming Pool<br>Services',
        'intro': 'MaxiCare provides comprehensive swimming pool services — from new pool construction and renovation to regular maintenance, water treatment and equipment repairs for villas, hotels and residential communities across the UAE.',
        'badge': 'Full construction, maintenance and repair under one team.',
        'features': [
            'New pool construction — concrete and fibreglass',
            'Pool renovation, resurfacing and tiling',
            'Regular maintenance: skimming, vacuuming, chemical balancing',
            'Water treatment and filtration system servicing',
            'Pump, filter and heater repair and replacement',
            'Pool lighting and automation system installation',
            'Green pool recovery and algae treatment',
        ],
        'why': 'The UAE\'s intense heat accelerates algae growth and chemical imbalance. MaxiCare\'s pool specialists ensure your pool remains safe, clean and inviting all year without you lifting a finger.',
    },
    {
        'slug': 'water-tank-cleaning',
        'name': 'Water Tank Cleaning',
        'icon': 'fa-tint',
        'cat': 'Water & Plumbing',
        'tagline': 'Safe, Clean Water For Every Property',
        'hero_txt': 'Water Tank<br>Cleaning',
        'intro': 'MaxiCare\'s water tank cleaning service ensures your property\'s stored water supply remains free from bacteria, sediment and contamination. We service domestic and commercial tanks of all sizes across Dubai, Abu Dhabi and Sharjah.',
        'badge': 'DM-compliant disinfection — certificate issued.',
        'features': [
            'Complete tank draining and high-pressure washing',
            'Disinfection with Dubai Municipality approved chemicals',
            'Sediment and biofilm removal from tank walls',
            'Inspection of float valves, inlet and outlet pipes',
            'Water sample testing before and after treatment',
            'Certificate of cleaning issued on completion',
            'Annual service contracts for property managers',
        ],
        'why': 'Contaminated water tanks are a serious health hazard. UAE regulations require regular tank cleaning and MaxiCare ensures full compliance — protecting your tenants and your liability.',
    },
    {
        'slug': 'duct-cleaning',
        'name': 'Duct Cleaning Services',
        'icon': 'fa-fan',
        'cat': 'Climate Control',
        'tagline': 'Breathe Cleaner Air. Every Day.',
        'hero_txt': 'Duct Cleaning<br>Services',
        'intro': 'Dirty air ducts accumulate dust, allergens, mould and bacteria — reducing air quality and AC efficiency. MaxiCare\'s duct cleaning service uses specialist equipment to thoroughly clean and sanitise your HVAC ductwork.',
        'badge': 'NADCA-method duct cleaning — before/after inspection included.',
        'features': [
            'Full ductwork inspection before and after cleaning',
            'High-powered negative pressure vacuum extraction',
            'Vent, grille and diffuser cleaning and disinfection',
            'Mould and bacteria treatment with approved sanitisers',
            'Coil cleaning for air handling units (AHUs)',
            'Filter replacement and upgraded filtration options',
            'Post-cleaning air quality assessment',
        ],
        'why': 'In the UAE, dust accumulation in ducts is relentless. Regular duct cleaning by MaxiCare not only improves air quality but can reduce AC energy consumption by up to 20%.',
    },
    {
        'slug': 'painting-services',
        'name': 'Painting Services',
        'icon': 'fa-paint-roller',
        'cat': 'Interiors',
        'tagline': 'Fresh Coats. Flawless Finish.',
        'hero_txt': 'Painting<br>Services',
        'intro': 'MaxiCare\'s painting team delivers high-quality interior and exterior paint jobs for villas, apartments, offices and commercial properties. We use premium paints with excellent coverage and durability suited to the UAE climate.',
        'badge': 'Premium paints — Jotun, Dulux and Berger available.',
        'features': [
            'Interior painting — walls, ceilings and woodwork',
            'Exterior painting with heat and UV-resistant paints',
            'Epoxy floor coating for garages and industrial spaces',
            'Texture finishes — stucco, venetian plaster, sand finish',
            'Wood staining, varnishing and lacquering',
            'Wallpaper installation and removal',
            'Colour consultation service available',
        ],
        'why': 'The UAE sun fades and degrades paint quickly. MaxiCare uses heat-resistant, high-quality paints and proper surface preparation to ensure your finish lasts for years — not months.',
    },
    {
        'slug': 'carpentry-services',
        'name': 'Carpentry Services',
        'icon': 'fa-hammer',
        'cat': 'Construction',
        'tagline': 'Precision Woodwork. Any Scale.',
        'hero_txt': 'Carpentry<br>Services',
        'intro': 'MaxiCare\'s carpentry team provides custom woodwork, furniture assembly, built-in wardrobes, kitchen cabinets, door repairs and full fit-outs for residential and commercial properties across the UAE.',
        'badge': 'Custom carpentry — from a single shelf to full fit-outs.',
        'features': [
            'Custom built-in wardrobes and cabinets',
            'Kitchen cabinet installation and modification',
            'Furniture assembly and disassembly',
            'Door repairs, replacement and new installation',
            'Flooring — laminate, hardwood and parquet laying',
            'False ceiling (gypsum) installation',
            'Office partitions and shopfitting',
        ],
        'why': 'Off-the-shelf furniture often doesn\'t fit UAE apartments and villas precisely. MaxiCare\'s skilled carpenters design and build to exact measurements — maximising space and quality.',
    },
    {
        'slug': 'landscaping',
        'name': 'Landscaping Services',
        'icon': 'fa-seedling',
        'cat': 'Outdoors',
        'tagline': 'Beautiful Outdoor Spaces, UAE-Tough',
        'hero_txt': 'Landscaping<br>Services',
        'intro': 'MaxiCare designs, installs and maintains outdoor spaces that thrive in the UAE climate — from villa gardens and pool surrounds to commercial green spaces and rooftop terraces.',
        'badge': 'UAE-adapted plants — drought-resistant and low-maintenance.',
        'features': [
            'Garden design and landscape planning',
            'Planting — trees, shrubs, ground cover and seasonal flowers',
            'Lawn installation and maintenance (natural and artificial)',
            'Drip irrigation system design and installation',
            'Hardscaping — paving, pathways and decking',
            'Outdoor lighting installation',
            'Regular garden maintenance contracts',
        ],
        'why': 'Landscaping in the UAE requires plants and systems specifically suited to extreme heat and limited rainfall. MaxiCare specifies drought-resistant species and efficient irrigation to keep costs down and gardens beautiful.',
    },
    {
        'slug': 'packing-moving',
        'name': 'Packing & Moving Services',
        'icon': 'fa-truck',
        'cat': 'Relocation',
        'tagline': 'Stress-Free Moves Across UAE',
        'hero_txt': 'Packing &amp; Moving<br>Services',
        'intro': 'MaxiCare takes the stress out of home and office relocations. Our professional team handles packing, transporting and unpacking your belongings safely — whether you\'re moving within the same building or across the UAE.',
        'badge': 'Fully insured moves — fragile items and furniture handled with care.',
        'features': [
            'Professional packing with quality materials',
            'Furniture disassembly and reassembly at destination',
            'Dedicated moving vehicles for all load sizes',
            'Fragile and valuable item specialist handling',
            'Office relocation with minimal business downtime',
            'Storage solutions during transition periods',
            'Intercity moves — Dubai, Abu Dhabi, Sharjah and beyond',
        ],
        'why': 'Moving in the UAE\'s heat is physically demanding and logistically complex. MaxiCare\'s experienced moving team ensures your possessions arrive safely and on time — every time.',
    },
    {
        'slug': 'water-proofing',
        'name': 'Water Proofing Services',
        'icon': 'fa-shield-alt',
        'cat': 'Construction',
        'tagline': 'Stop Water Damage Before It Starts',
        'hero_txt': 'Water Proofing<br>Services',
        'intro': 'MaxiCare\'s waterproofing division protects roofs, bathrooms, wet areas, foundations and external walls from moisture infiltration — preventing structural damage, mould and costly repairs.',
        'badge': 'System warranties available — long-term protection guaranteed.',
        'features': [
            'Roof and terrace waterproofing — bitumen and liquid membrane',
            'Bathroom and wet area waterproofing',
            'External wall sealing and façade protection',
            'Foundation and basement waterproofing',
            'Swimming pool waterproofing and resurfacing',
            'Water tank lining and sealing',
            'Crack injection and structural repair',
        ],
        'why': 'Even in a dry climate, the UAE\'s intense summer rains and building movement cause moisture infiltration. Early waterproofing investment saves thousands in future structural repairs.',
    },
    {
        'slug': 'interior-design',
        'name': 'Interior Design',
        'icon': 'fa-couch',
        'cat': 'Interiors',
        'tagline': 'Spaces Designed For How You Live',
        'hero_txt': 'Interior Design<br>Services',
        'intro': 'MaxiCare\'s interior design team transforms residential and commercial spaces with creative concepts, practical layouts and carefully selected materials — from consultation and 3D visualisation to complete fit-out.',
        'badge': 'Concept to completion — design and execution by one team.',
        'features': [
            'Space planning and 3D design visualisation',
            'Residential interior design for villas and apartments',
            'Commercial design — offices, retail, hospitality',
            'Material and finish specification (flooring, tiles, paint)',
            'Custom furniture and joinery design',
            'Lighting design and specification',
            'Project management and fit-out coordination',
        ],
        'why': 'Great interior design maximises both the aesthetic and functional potential of a space. MaxiCare\'s in-house team handles everything — from the first sketch to the final installation — keeping your project on time and on budget.',
    },
    {
        'slug': 'marble-care',
        'name': 'Marble Care Services',
        'icon': 'fa-gem',
        'cat': 'Cleaning & Hygiene',
        'tagline': 'Restore the Natural Beauty of Stone',
        'hero_txt': 'Marble Care<br>Services',
        'intro': 'MaxiCare\'s marble care specialists restore and maintain marble, granite, limestone and terrazzo surfaces — eliminating scratches, stains and dullness to bring back their natural lustre.',
        'badge': 'All natural stone types treated — floor, wall and countertop.',
        'features': [
            'Marble polishing and crystallization',
            'Diamond grinding to remove deep scratches and lippage',
            'Honing for a matte or satin finish',
            'Stain removal and poultice treatment',
            'Crack repair and chip filling',
            'Sealing to protect against future staining',
            'Maintenance contracts for hotels and commercial properties',
        ],
        'why': 'Marble is beautiful but high-maintenance in the UAE\'s dusty environment. Regular professional care by MaxiCare prevents permanent damage and maintains the value of your stone floors and surfaces.',
    },
    {
        'slug': 'maid-services',
        'name': 'Maid Services',
        'icon': 'fa-home',
        'cat': 'Cleaning & Hygiene',
        'tagline': 'Your Home, Immaculate. Always.',
        'hero_txt': 'Maid<br>Services',
        'intro': 'MaxiCare provides trained, background-checked maids for regular housekeeping, one-time deep cleans, post-party cleaning and move-in / move-out cleaning across Dubai, Abu Dhabi and Sharjah.',
        'badge': 'Background-checked, trained maids — on-demand or regular schedule.',
        'features': [
            'Regular housekeeping — daily, weekly or bi-weekly',
            'One-time deep cleaning (rooms, kitchens, bathrooms)',
            'Post-party and post-event cleaning',
            'Move-in / move-out cleaning',
            'Ironing and laundry assistance',
            'Fridge, oven and appliance cleaning',
            'Flexible hours including evenings and weekends',
        ],
        'why': 'A clean, well-maintained home improves wellbeing and reduces stress. MaxiCare\'s maids are thoroughly vetted and trained to work efficiently and respectfully in your home.',
    },
    {
        'slug': 'facility-management',
        'name': 'Facility Management',
        'icon': 'fa-building',
        'cat': 'Management',
        'tagline': 'Total Property Management. One Partner.',
        'hero_txt': 'Facility<br>Management',
        'intro': 'MaxiCare delivers end-to-end facility management for commercial complexes, residential communities, schools, hospitals and hotels. Our structured AMC packages bundle multiple services into a single, cost-effective contract.',
        'badge': 'Tailored AMC packages — multi-service, predictable costs.',
        'features': [
            'Annual Maintenance Contracts (AMC) — customised bundles',
            'Preventive maintenance scheduling and tracking',
            'Emergency response coordination across all services',
            'Dedicated account manager for each facility',
            'Energy management and efficiency reporting',
            'Compliance with UAE regulatory requirements',
            'Sector-specific expertise: healthcare, education, retail, hospitality',
        ],
        'why': 'Managing a facility means coordinating dozens of services simultaneously. MaxiCare\'s centralised management model gives you one point of contact, one invoice and guaranteed service levels — simplifying property operations completely.',
    },
    {
        'slug': 'electronics-repair',
        'name': 'Electronics Repair',
        'icon': 'fa-tools',
        'cat': 'Technical',
        'tagline': 'Fix It Fast. Fix It Right.',
        'hero_txt': 'Electronics &amp; Appliance<br>Repair',
        'intro': 'MaxiCare\'s electronics repair technicians diagnose and fix household appliances, televisions, washing machines, refrigerators, dishwashers and other electronic equipment — saving you the cost of replacement.',
        'badge': 'Multi-brand repair — all major household appliances covered.',
        'features': [
            'Washing machine and dryer repair',
            'Refrigerator and freezer repair',
            'Dishwasher repair and servicing',
            'Television diagnosis and repair',
            'Water heater and immersion heater repair',
            'Microwave and oven repair',
            'General electronic fault diagnosis',
        ],
        'why': 'Appliance replacement is expensive. MaxiCare\'s skilled technicians can often repair faulty appliances at a fraction of the replacement cost — with a warranty on all repairs.',
    },
    {
        'slug': 'fountains-water-features',
        'name': 'Fountains & Water Features',
        'icon': 'fa-water',
        'cat': 'Water & Plumbing',
        'tagline': 'Elegant Water Features, Expertly Installed',
        'hero_txt': 'Fountains &amp; Water<br>Features',
        'intro': 'MaxiCare designs, supplies, installs and maintains decorative indoor and outdoor water features — from entry fountains and garden cascades to indoor wall features and courtyard water installations.',
        'badge': 'Custom design and installation — complete maintenance packages.',
        'features': [
            'Custom fountain design and engineering',
            'Indoor and outdoor water feature installation',
            'Pump and filtration system selection and installation',
            'Lighting integration for evening ambience',
            'Maintenance contracts — cleaning, chemical treatment',
            'Repair of existing fountain systems and pumps',
            'Water feature renovation and modernisation',
        ],
        'why': 'Water features are a powerful design element in UAE properties — creating calm in the heat and elevating property value. MaxiCare handles everything from concept through ongoing maintenance.',
    },
    {
        'slug': 'hygiene-care',
        'name': 'Hygiene Care Services',
        'icon': 'fa-hand-sparkles',
        'cat': 'Cleaning & Hygiene',
        'tagline': 'Sanitation Standards That Protect People',
        'hero_txt': 'Hygiene Care<br>Services',
        'intro': 'MaxiCare\'s hygiene care division provides deep sanitisation and disinfection for commercial kitchens, restaurants, gyms, schools, offices and healthcare facilities — ensuring compliance with UAE health standards.',
        'badge': 'Dubai Municipality compliant — certificates available.',
        'features': [
            'Commercial kitchen deep cleaning and sanitisation',
            'Restaurant and food preparation area disinfection',
            'Gym and locker room sanitisation',
            'School and nursery deep cleaning',
            'Office and healthcare facility disinfection',
            'Electrostatic spraying for rapid surface sanitisation',
            'Scheduled hygiene contracts with compliance certificates',
        ],
        'why': 'UAE food safety and health regulations require documented hygiene management. MaxiCare\'s certified hygiene care team ensures your premises meet regulatory standards — protecting your staff, customers and licence.',
    },
    {
        'slug': 'building-contracting',
        'name': 'Building Contracting',
        'icon': 'fa-hard-hat',
        'cat': 'Construction',
        'tagline': 'Build. Renovate. Transform.',
        'hero_txt': 'Building<br>Contracting',
        'intro': 'MaxiCare\'s licensed contracting team undertakes renovation, fit-out, extension and new construction projects for residential and commercial clients across Dubai, Abu Dhabi and Sharjah.',
        'badge': 'Licensed UAE contractor — all permits handled.',
        'features': [
            'Villa and apartment renovation and refurbishment',
            'Commercial fit-out and office refurbishment',
            'Structural modifications and extensions',
            'Demolition and strip-out',
            'Civil works — concrete, blockwork, plastering',
            'Full project management from planning to handover',
            'Permit coordination with Dubai Municipality / DDA',
        ],
        'why': 'Construction projects in the UAE require navigating complex permitting and regulatory requirements. MaxiCare\'s experienced contracting team manages the entire process — delivering on time and within budget.',
    },
    {
        'slug': 'furniture-maintenance',
        'name': 'Furniture Maintenance',
        'icon': 'fa-chair',
        'cat': 'Interiors',
        'tagline': 'Restore, Repair, Renew Your Furniture',
        'hero_txt': 'Furniture<br>Maintenance',
        'intro': 'MaxiCare\'s furniture specialists repair, restore and reupholster home and office furniture — extending its life and saving you the cost of replacement. We work with wood, fabric, leather and rattan.',
        'badge': 'Home and office furniture — all materials treated.',
        'features': [
            'Wood furniture repair and restoration',
            'Sofa and chair reupholstery — fabric and leather',
            'Polish and lacquer refinishing for wooden surfaces',
            'Structural repair of broken frames and joints',
            'Cushion and foam replacement',
            'Office chair and workstation maintenance',
            'Antique and high-value piece restoration',
        ],
        'why': 'Quality furniture is a significant investment. MaxiCare\'s craftsmen can restore even heavily worn pieces to near-original condition — at a fraction of the replacement cost.',
    },
    {
        'slug': 'scotch-guard',
        'name': 'Scotch Guard Services',
        'icon': 'fa-spray-can',
        'cat': 'Cleaning & Hygiene',
        'tagline': 'Protect Fabrics Before Stains Strike',
        'hero_txt': 'Scotch Guard<br>Fabric Protection',
        'intro': 'MaxiCare applies professional-grade Scotch Guard fabric protection to sofas, carpets, rugs, curtains and upholstery — creating an invisible barrier that repels liquids, stains and allergens.',
        'badge': 'All fabric types treated — home and office.',
        'features': [
            'Scotch Guard application to sofas and armchairs',
            'Carpet and rug fabric protection treatment',
            'Curtain and drape protection',
            'Car seat and interior fabric treatment',
            'Mattress protection application',
            'Combined cleaning and protection packages',
            'Re-treatment service after professional cleaning',
        ],
        'why': 'Fabric protection is far cheaper than professional stain removal or furniture replacement. MaxiCare\'s treatment creates an invisible shield that gives you time to blot spills before they set — perfect for homes with children or pets.',
    },
]

# Template for each service page
def build_page(s):
    # SVG checkmark items — stagger delay via CSS --i custom property
    features_html = '\n'.join(
        f'<li class="check-item flex items-start gap-3" style="--i:{i}">'
        f'<svg class="check-svg flex-shrink-0 mt-0.5" width="22" height="22" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">'
        f'<circle cx="12" cy="12" r="10" stroke="#1a3c5e" stroke-width="1.5" opacity="0.25"/>'
        f'<path class="check-path" d="M5.5 12.5L9.5 16.5L18.5 7.5" stroke="#1a3c5e" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
        f'</svg>'
        f'<span>{f}</span></li>'
        for i, f in enumerate(s['features'])
    )

    # Split hero_txt on <br> for GSAP line-by-line reveal
    hero_lines = s['hero_txt'].split('<br>')
    hero_h1_inner = '\n'.join(
        f'        <span class="hero-line-wrap"><span class="hero-word">{line}</span></span>'
        for line in hero_lines
    )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="canonical" href="https://maxicare-uae.pages.dev/pages/{s['slug']}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://maxicare-uae.pages.dev/pages/{s['slug']}">
    <meta property="og:title" content="{s['name']} UAE | MaxiCare Facility Management">
    <meta property="og:description" content="{s['intro'][:160]}">
    <meta property="og:image" content="https://maxicare-uae.pages.dev/assets/hero.jpg">
    <meta property="og:site_name" content="MaxiCare UAE">
    <meta property="og:locale" content="en_AE">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{s['name']} UAE | MaxiCare">
    <meta name="twitter:description" content="{s['intro'][:160]}">
    <meta name="twitter:image" content="https://maxicare-uae.pages.dev/assets/hero.jpg">
    <title>{s['name']} in Dubai, Abu Dhabi &amp; Sharjah | MaxiCare UAE</title>
    <meta name="description" content="{s['intro'][:155]}">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": "{s['name']}",
        "name": "{s['name']}",
        "description": "{s['intro'][:200]}",
        "provider": {{
            "@type": "LocalBusiness",
            "name": "MaxiCare UAE",
            "url": "https://maxicare-uae.pages.dev",
            "telephone": "+97142990440",
            "email": "info@maxicareme.com",
            "address": [{{"@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE"}},{{"@type": "PostalAddress", "addressLocality": "Abu Dhabi", "addressCountry": "AE"}}]
        }},
        "areaServed": [{{"@type": "Country", "name": "UAE"}},{{"@type": "City", "name": "Dubai"}},{{"@type": "City", "name": "Abu Dhabi"}},{{"@type": "City", "name": "Sharjah"}}],
        "url": "https://maxicare-uae.pages.dev/pages/{s['slug']}"
    }}
    </script>
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://maxicare-uae.pages.dev/"}},
            {{"@type": "ListItem", "position": 2, "name": "Services", "item": "https://maxicare-uae.pages.dev/#services"}},
            {{"@type": "ListItem", "position": 3, "name": "{s['name']}", "item": "https://maxicare-uae.pages.dev/pages/{s['slug']}"}}
        ]
    }}
    </script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="../assets/css/style.css">
    <style>
    /* ── SVG checkmark draw ─────────────────────────────────────────── */
    .check-svg .check-path {{
        stroke-dasharray: 30;
        stroke-dashoffset: 30;
        transition: stroke-dashoffset 0.55s cubic-bezier(0.22, 1, 0.36, 1);
    }}
    .check-item.visible .check-path {{ stroke-dashoffset: 0; }}

    /* ── Check-item slide from left ─────────────────────────────────── */
    .check-item {{
        opacity: 0;
        transform: translateX(-20px);
        transition:
            opacity  0.45s ease calc(var(--i) * 80ms),
            transform 0.45s ease calc(var(--i) * 80ms);
    }}
    .check-item.visible {{ opacity: 1; transform: translateX(0); }}

    /* ── Hero category tag fade-up ──────────────────────────────────── */
    .hero-tag {{
        opacity: 0;
        transform: translateY(8px);
        transition: opacity 0.6s ease 0.1s, transform 0.6s ease 0.1s;
    }}
    .hero-tag.visible {{ opacity: 1; transform: translateY(0); }}

    /* ── Why MaxiCare border-left draw ──────────────────────────────── */
    .why-block {{
        position: relative;
        padding-left: 1.25rem;
    }}
    .why-block::before {{
        content: '';
        position: absolute;
        left: 0; top: 0;
        width: 4px; height: 100%;
        background: linear-gradient(to bottom, #d97706, #1a3c5e);
        border-radius: 2px;
        transform: scaleY(0);
        transform-origin: top center;
        transition: transform 0.7s cubic-bezier(0.22, 1, 0.36, 1) 0.1s;
    }}
    .why-block.visible::before {{ transform: scaleY(1); }}

    /* ── CTA background pulse ───────────────────────────────────────── */
    @keyframes ctaPulse {{
        0%, 100% {{ background-position: 0% 50%; }}
        50%       {{ background-position: 100% 50%; }}
    }}
    .cta-section {{
        background: linear-gradient(135deg, #f9fafb, #eff6ff, #fef3c7, #f9fafb);
        background-size: 400% 400%;
        animation: ctaPulse 8s ease infinite;
    }}

    @media (prefers-reduced-motion: reduce) {{
        .check-item, .hero-tag {{ transition: none; }}
        .why-block::before {{ transition: none; }}
        .cta-section {{ animation: none; background: #f9fafb; }}
    }}
    </style>
</head>
<body class="bg-white text-[#1a1a1a]">

    <a href="https://wa.me/971525243091" class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
        <i class="fab fa-whatsapp" aria-hidden="true"></i>
    </a>

    <nav class="flex items-center justify-between px-6 md:px-8 py-4 max-w-7xl mx-auto w-full">
        <a href="../index.html" class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl flex items-center justify-center flex-shrink-0" style="background:#1a3c5e">
                <span class="text-white font-black text-sm tracking-tighter">MC</span>
            </div>
            <span class="text-lg font-black tracking-tighter uppercase">Maxi<span class="font-light">Care</span></span>
        </a>
        <div class="hidden md:flex items-center space-x-6 text-xs font-bold uppercase tracking-widest">
            <a href="../index.html#services" class="hover:text-amber-700 transition-colors duration-200">Services</a>
            <a href="../index.html#why-us" class="hover:text-amber-700 transition-colors duration-200">Why Us</a>
            <a href="../index.html#contact" class="hover:text-amber-700 transition-colors duration-200">Coverage</a>
            <a href="../index.html#contact" class="text-white px-5 py-2 rounded-full hover:opacity-90 transition-opacity duration-200" style="background:#1a3c5e">Get Free Quote</a>
        </div>
    </nav>

    <main>
        <!-- Breadcrumb -->
        <div class="bg-gray-50 border-b border-gray-100 py-3 px-4">
            <div class="max-w-7xl mx-auto text-xs font-bold uppercase tracking-widest text-gray-500">
                <a href="../index.html" class="hover:text-amber-700 transition-colors duration-200">Home</a>
                <span class="mx-2">›</span>
                <a href="../index.html#services" class="hover:text-amber-700 transition-colors duration-200">Services</a>
                <span class="mx-2">›</span>
                <span style="color:#1a3c5e">{s['name']}</span>
            </div>
        </div>

        <!-- Page Hero -->
        <section class="py-20 px-4 text-center overflow-hidden" style="background:#1a3c5e">
            <p class="hero-tag text-amber-300 text-sm font-bold tracking-[0.3em] uppercase mb-3">{s['cat']}</p>
            <h1 class="text-4xl md:text-5xl font-black text-white uppercase tracking-tighter mb-3 leading-tight">
{hero_h1_inner}
            </h1>
            <p class="text-blue-200 text-lg mb-8 max-w-xl mx-auto">{s['tagline']}</p>
            <a href="../index.html#contact" class="inline-flex items-center gap-3 bg-white px-8 py-4 rounded-full font-bold text-sm uppercase tracking-widest hover:bg-amber-50 transition-colors duration-200" style="color:#1a3c5e">
                Get a Free Quote <i class="fas fa-arrow-right text-xs"></i>
            </a>
        </section>

        <!-- Content -->
        <section class="py-20 px-4">
            <div class="max-w-4xl mx-auto">
                <div class="grid md:grid-cols-2 gap-16 items-start">
                    <div>
                        <h2 class="text-3xl font-black uppercase mb-6 leading-tight">{s['name']}</h2>
                        <p class="text-gray-600 leading-relaxed text-base mb-8">{s['intro']}</p>
                        <div class="flex items-center gap-3 p-5 rounded-2xl border" style="background:#eff6ff;border-color:#bfdbfe">
                            <div class="w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0" style="background:#1a3c5e">
                                <i class="fas fa-certificate text-white text-sm"></i>
                            </div>
                            <p class="text-sm font-bold" style="color:#1a3c5e">{s['badge']}</p>
                        </div>
                        <div class="why-block mt-8 p-5 rounded-2xl bg-amber-50 border border-amber-100">
                            <h4 class="text-xs font-black uppercase tracking-widest text-amber-800 mb-3">Why MaxiCare for This Service</h4>
                            <p class="text-sm text-amber-900 leading-relaxed">{s['why']}</p>
                        </div>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold tracking-[0.3em] uppercase mb-6" style="color:#1a3c5e">What\'s Included</h3>
                        <ul class="space-y-4 text-sm text-gray-700 leading-relaxed">
                            {features_html}
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Contact CTA -->
        <section class="cta-section py-16 px-4 text-center">
            <h2 class="text-3xl font-black uppercase mb-4">Ready to Book?</h2>
            <p class="text-gray-500 text-sm mb-8 max-w-md mx-auto">Call or WhatsApp MaxiCare now for a free, no-obligation quote on {s['name'].lower()} across Dubai, Abu Dhabi and Sharjah.</p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="tel:8002012" class="inline-flex items-center justify-center gap-3 text-white px-8 py-4 rounded-full font-bold text-sm uppercase tracking-widest hover:opacity-90 transition-opacity duration-200" style="background:#1a3c5e">
                    <i class="fas fa-phone text-xs"></i> Call 8002012
                </a>
                <a href="https://wa.me/971525243091" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-3 bg-green-500 text-white px-8 py-4 rounded-full font-bold text-sm uppercase tracking-widest hover:bg-green-600 transition-colors duration-200">
                    <i class="fab fa-whatsapp"></i> WhatsApp Us
                </a>
            </div>
        </section>

        <!-- Back to services -->
        <div class="py-8 px-4 text-center border-t border-gray-100">
            <a href="../index.html#services" class="inline-flex items-center gap-2 text-sm font-bold uppercase tracking-widest hover:opacity-70 transition-opacity duration-200" style="color:#1a3c5e">
                <i class="fas fa-arrow-left text-xs"></i> All Services
            </a>
        </div>
    </main>

    <footer class="py-8 px-4 text-center" style="background:#1a3c5e">
        <div class="max-w-7xl mx-auto">
            <p class="text-gray-300 text-xs mb-2">&copy; 2025 MaxiCare UAE — {s['name']} Dubai, Abu Dhabi &amp; Sharjah</p>
            <p class="text-gray-400 text-xs">Toll Free: 8002012 &nbsp;|&nbsp; <a href="mailto:info@maxicareme.com" class="hover:text-amber-400 transition-colors duration-200">info@maxicareme.com</a></p>
        </div>
    </footer>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script>
    // Hero: category tag fade-up
    document.querySelector('.hero-tag').classList.add('visible');

    // Hero H1: GSAP line reveal
    gsap.fromTo('.hero-word',
        {{ yPercent: 110, opacity: 0 }},
        {{ yPercent: 0, opacity: 1, duration: 0.9, ease: 'power3.out', stagger: 0.15, delay: 0.2 }}
    );

    // Scroll-triggered: check items + why block
    const io = new IntersectionObserver((entries) => {{
        entries.forEach(e => {{
            if (e.isIntersecting) {{
                e.target.classList.add('visible');
                io.unobserve(e.target);
            }}
        }});
    }}, {{ threshold: 0.12 }});

    document.querySelectorAll('.check-item, .why-block').forEach(el => io.observe(el));
    </script>

</body>
</html>'''


os.makedirs('pages', exist_ok=True)
for s in SERVICES:
    path = f'pages/{s["slug"]}.html'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(build_page(s))
    print(f'  Created: {path}')

print(f'\nDone — {len(SERVICES)} service pages created.')
