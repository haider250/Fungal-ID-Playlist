import React, { useState } from 'react';
import { 
  Search, Plus, X, BookOpen, AlertCircle, Lightbulb, 
  Microscope, Eye, Leaf, Download, Filter, ChevronDown, 
  ChevronUp, Trash2, Edit3, Save 
} from 'lucide-react';

// Types
interface FungalEntry {
  id: number;
  scientificName: string;
  commonName: string;
  phylum: string;
  class: string;
  order: string;
  family: string;
  student: string;
  date: string;
  habitat: string;
  substrate: string;
  macroFeatures: string[];
  microFeatures: string[];
  sporeDetails: string;
  reproductiveStructures: string;
  keyDiagnostic: string[];
  distinguishingFeatures: string;
  mnemonic: string;
  commonMistakes: string;
  ecologicalRole: string;
  medicalRelevance: string;
  industrialUse: string;
  season: string;
  distribution: string;
  imageNotes: string;
}

// Constants
const PHYLA = ['All', 'Ascomycota', 'Basidiomycota', 'Zygomycota', 'Chytridiomycota', 'Glomeromycota'];
const HABITATS = ['All', 'Soil', 'Wood', 'Leaf litter', 'Dung', 'Aquatic', 'Indoor', 'Parasitic', 'Mycorrhizal'];
const SEASONS = ['Spring', 'Summer', 'Fall', 'Winter', 'Year-round'];
const ECOLOGICAL_ROLES = ['Saprotroph', 'Mycorrhizal', 'Parasitic', 'Pathogenic', 'Endophytic', 'Lichens'];

// Initial Data
const INITIAL_ENTRIES: FungalEntry[] = [
  {
    id: 1,
    scientificName: "Amanita muscaria",
    commonName: "Fly Agaric",
    phylum: "Basidiomycota",
    class: "Agaricomycetes",
    order: "Agaricales",
    family: "Amanitaceae",
    student: "Mycologist Example",
    date: "2024-11-10",
    habitat: "Coniferous and deciduous forests, mycorrhizal with trees",
    substrate: "Soil, associated with tree roots",
    macroFeatures: ["Bright red cap with white warts", "White gills", "Bulbous base with volva", "White stalk with ring"],
    microFeatures: ["White spore print", "Ellipsoid spores", "Clamp connections present"],
    sporeDetails: "Ellipsoid, 9-13 x 6.5-9 μm, smooth, inamyloid",
    reproductiveStructures: "Basidia 4-spored, basidiospores produced on gills",
    keyDiagnostic: ["Red cap with white spots", "White gills free from stalk", "Bulbous base with volva"],
    distinguishingFeatures: "Distinctive red cap with white warts; differs from edible Amanita caesarea by cap color and habitat",
    mnemonic: "Christmas mushroom - red and white like Santa! TOXIC!",
    commonMistakes: "Often confused with edible Amanitas but highly toxic; distinct from A. pantherina by red coloration",
    ecologicalRole: "Mycorrhizal",
    medicalRelevance: "Hallucinogenic, toxic; contains muscimol and ibotenic acid",
    industrialUse: "Used in traditional practices, not commercially cultivated",
    season: "Late Summer-Fall",
    distribution: "Northern Hemisphere cosmopolitan",
    imageNotes: "Photograph cap showing warts and gill attachment; microscopic spores at 400x"
  },
  {
    id: 2,
    scientificName: "Ganoderma lucidum",
    commonName: "Reishi Mushroom",
    phylum: "Basidiomycota",
    class: "Agaricomycetes",
    order: "Polyporales",
    family: "Ganodermataceae",
    student: "Herbalist Student",
    date: "2024-11-09",
    habitat: "Hardwood forests, on logs and stumps",
    substrate: "Dead hardwood (oak, maple)",
    macroFeatures: ["Lacquer-red kidney-shaped cap", "Woody texture", "No stalk or lateral stalk", "Pore surface white"],
    microFeatures: ["Brown spore print", "Double-walled spores", "Trimitic hyphal system"],
    sporeDetails: "Ellipsoid with truncated end, 8.5-11.5 x 5-7 μm, brown, double-walled",
    reproductiveStructures: "Basidiospores produced in pores on underside",
    keyDiagnostic: ["Lacquer-like shiny cap", "Woody texture", "White pore surface"],
    distinguishingFeatures: "Shiny lacquered appearance distinguishes from other Ganoderma species",
    mnemonic: "Lucidum = shiny - remember the lacquered look!",
    commonMistakes: "Confused with Ganoderma tsugae (on hemlock) and G. sessile (different habitat)",
    ecologicalRole: "Saprotroph on hardwoods",
    medicalRelevance: "Medicinal mushroom used in traditional Chinese medicine for immunity",
    industrialUse: "Dietary supplements, tea extracts",
    season: "Year-round, perennial",
    distribution: "Temperate and tropical regions worldwide",
    imageNotes: "Show lacquered cap surface and pore layer; spores need high magnification"
  },
  // Add 28 more entries here in the same structure...
  {
    id: 3,
    scientificName: "Pleurotus ostreatus",
    commonName: "Oyster Mushroom",
    phylum: "Basidiomycota",
    class: "Agaricomycetes",
    order: "Agaricales",
    family: "Pleurotaceae",
    student: "Cultivation Researcher",
    date: "2024-11-08",
    habitat: "Hardwood forests, dead trees",
    substrate: "Dead hardwood logs",
    macroFeatures: ["Shell-shaped cap", "White to gray coloration", "Decurrent gills", "Lateral or absent stalk"],
    microFeatures: ["Lilac-gray spore print", "Cylindrical spores", "Clamp connections"],
    sporeDetails: "Cylindrical, 7.5-10 x 3-4 μm, smooth, hyaline",
    reproductiveStructures: "Basidia 4-spored, gills decurrent",
    keyDiagnostic: ["Shell-shaped cap", "Decurrent gills", "Grows on wood"],
    distinguishingFeatures: "Lacks the deadly amatoxins of similar-looking white mushrooms; edible and commonly cultivated",
    mnemonic: "Oyster shape, oyster color - safe and delicious!",
    commonMistakes: "Young specimens confused with poisonous white mushrooms but always grows on wood",
    ecologicalRole: "Saprotroph on hardwoods",
    medicalRelevance: "Edible, contains statins and antioxidants",
    industrialUse: "Commercial cultivation, bioremediation",
    season: "Spring-Fall",
    distribution: "Worldwide",
    imageNotes: "Show gill attachment and growth on wood; spore print lilac-gray"
  }
  // ... continue with 27 more diverse fungal entries
];

// Components
const Header: React.FC<{ onExport: () => void }> = ({ onExport }) => (
  <div className="bg-white rounded-lg shadow-xl p-8 mb-6 border-t-4 border-green-600">
    <div className="flex items-center justify-between">
      <div>
        <h1 className="text-4xl font-bold text-green-800 mb-2">🍄 Comprehensive Fungal ID Playlist</h1>
        <p className="text-gray-600 text-lg">A detailed collaborative database of identified fungal specimens</p>
      </div>
      <button
        onClick={onExport}
        className="px-4 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700 flex items-center gap-2 transition-colors"
      >
        <Download size={20} />
        Export Data
      </button>
    </div>
  </div>
);

const SearchAndFilterBar: React.FC<{
  searchTerm: string;
  onSearchChange: (value: string) => void;
  selectedPhylum: string;
  onPhylumChange: (value: string) => void;
  selectedHabitat: string;
  onHabitatChange: (value: string) => void;
  sortBy: string;
  onSortChange: (value: string) => void;
  onAddEntry: () => void;
}> = ({
  searchTerm,
  onSearchChange,
  selectedPhylum,
  onPhylumChange,
  selectedHabitat,
  onHabitatChange,
  sortBy,
  onSortChange,
  onAddEntry
}) => (
  <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
    <div className="grid md:grid-cols-2 lg:grid-cols-5 gap-4">
      <div className="lg:col-span-2 relative">
        <Search className="absolute left-3 top-3 text-gray-400" size={20} />
        <input
          type="text"
          placeholder="Search by scientific name, common name, or family..."
          className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition-all"
          value={searchTerm}
          onChange={(e) => onSearchChange(e.target.value)}
        />
      </div>
      <select
        className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 transition-all"
        value={selectedPhylum}
        onChange={(e) => onPhylumChange(e.target.value)}
      >
        {PHYLA.map(p => <option key={p} value={p}>Phylum: {p}</option>)}
      </select>
      <select
        className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 transition-all"
        value={selectedHabitat}
        onChange={(e) => onHabitatChange(e.target.value)}
      >
        {HABITATS.map(h => <option key={h} value={h}>Habitat: {h}</option>)}
      </select>
      <button
        onClick={onAddEntry}
        className="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 flex items-center gap-2 justify-center font-medium transition-colors"
      >
        <Plus size={20} />
        Add Entry
      </button>
    </div>
    <div className="mt-4 flex items-center gap-4">
      <span className="text-sm text-gray-600 font-medium">Sort by:</span>
      {['date', 'name', 'phylum'].map(sortOption => (
        <button
          key={sortOption}
          onClick={() => onSortChange(sortOption)}
          className={`px-3 py-1 rounded transition-colors ${
            sortBy === sortOption ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
          }`}
        >
          {sortOption === 'date' ? 'Date Added' : sortOption === 'name' ? 'Scientific Name' : 'Phylum'}
        </button>
      ))}
    </div>
  </div>
);

const StatsDashboard: React.FC<{ entries: FungalEntry[] }> = ({ entries }) => {
  const stats = {
    totalSpecies: entries.length,
    phyla: new Set(entries.map(e => e.phylum)).size,
    memoryTricks: entries.filter(e => e.mnemonic).length,
    mistakeAlerts: entries.filter(e => e.commonMistakes).length,
    contributors: new Set(entries.map(e => e.student)).size,
  };

  return (
    <div className="grid grid-cols-2 md:grid-cols-5 gap-4 mb-6">
      {[
        { label: 'Total Species', value: stats.totalSpecies, color: 'green' },
        { label: 'Phyla', value: stats.phyla, color: 'blue' },
        { label: 'Memory Tricks', value: stats.memoryTricks, color: 'purple' },
        { label: 'Mistake Alerts', value: stats.mistakeAlerts, color: 'orange' },
        { label: 'Contributors', value: stats.contributors, color: 'teal' },
      ].map((stat, index) => (
        <div
          key={stat.label}
          className={`bg-white rounded-lg shadow-lg p-4 text-center border-t-4 border-${stat.color}-500`}
        >
          <div className={`text-3xl font-bold text-${stat.color}-600`}>{stat.value}</div>
          <div className="text-sm text-gray-600 font-medium">{stat.label}</div>
        </div>
      ))}
    </div>
  );
};

const EntryCard: React.FC<{
  entry: FungalEntry;
  isExpanded: boolean;
  onToggle: (id: number) => void;
  onDelete: (id: number) => void;
}> = ({ entry, isExpanded, onToggle, onDelete }) => (
  <div className="bg-white rounded-lg shadow-lg hover:shadow-xl transition-all duration-300">
    <div className="p-6 cursor-pointer" onClick={() => onToggle(entry.id)}>
      <div className="flex items-center justify-between">
        <div className="flex-1">
          <div className="flex items-center gap-4 mb-2">
            <h3 className="text-xl font-bold text-gray-900">{entry.scientificName}</h3>
            <span className="px-2 py-1 bg-green-100 text-green-800 text-sm rounded-full">
              {entry.commonName}
            </span>
          </div>
          <div className="flex flex-wrap gap-4 text-sm text-gray-600">
            <span className="flex items-center gap-1">
              <Leaf size={16} />
              {entry.phylum}
            </span>
            <span>📅 {entry.date}</span>
            <span>🧑‍🎓 {entry.student}</span>
            <span>🏞️ {entry.habitat}</span>
          </div>
        </div>
        <div className="flex items-center gap-2">
          <button
            onClick={(e) => {
              e.stopPropagation();
              onDelete(entry.id);
            }}
            className="p-2 text-red-500 hover:bg-red-50 rounded-lg transition-colors"
          >
            <Trash2 size={20} />
          </button>
          <ChevronDown
            size={20}
            className={`text-gray-500 transition-transform ${isExpanded ? 'rotate-180' : ''}`}
          />
        </div>
      </div>
    </div>

    {isExpanded && (
      <div className="px-6 pb-6 border-t pt-6">
        <div className="grid md:grid-cols-2 gap-6">
          {/* Taxonomy Section */}
          <div className="space-y-4">
            <Section title="Taxonomy" icon={BookOpen}>
              <InfoRow label="Class" value={entry.class} />
              <InfoRow label="Order" value={entry.order} />
              <InfoRow label="Family" value={entry.family} />
            </Section>

            <Section title="Habitat & Ecology" icon={Leaf}>
              <InfoRow label="Substrate" value={entry.substrate} />
              <InfoRow label="Ecological Role" value={entry.ecologicalRole} />
              <InfoRow label="Season" value={entry.season} />
              <InfoRow label="Distribution" value={entry.distribution} />
            </Section>

            <Section title="Macroscopic Features" icon={Eye}>
              <FeatureList features={entry.macroFeatures} />
            </Section>
          </div>

          <div className="space-y-4">
            <Section title="Microscopic Features" icon={Microscope}>
              <FeatureList features={entry.microFeatures} />
              <InfoRow label="Spore Details" value={entry.sporeDetails} />
              <InfoRow label="Reproductive Structures" value={entry.reproductiveStructures} />
            </Section>

            <Section title="Identification Keys" icon={Filter}>
              <FeatureList features={entry.keyDiagnostic} />
              <InfoRow label="Distinguishing Features" value={entry.distinguishingFeatures} />
            </Section>

            <Section title="Learning Aids" icon={Lightbulb}>
              <InfoRow label="Mnemonic" value={entry.mnemonic} />
              <InfoRow label="Common Mistakes" value={entry.commonMistakes} />
              <InfoRow label="Image Notes" value={entry.imageNotes} />
            </Section>

            <Section title="Applied Mycology" icon={AlertCircle}>
              <InfoRow label="Medical Relevance" value={entry.medicalRelevance} />
              <InfoRow label="Industrial Use" value={entry.industrialUse} />
            </Section>
          </div>
        </div>
      </div>
    )}
  </div>
);

const Section: React.FC<{ title: string; icon: React.ElementType; children: React.ReactNode }> = ({ 
  title, 
  icon: Icon, 
  children 
}) => (
  <div>
    <h4 className="flex items-center gap-2 text-lg font-semibold text-gray-800 mb-3">
      <Icon size={20} className="text-green-600" />
      {title}
    </h4>
    {children}
  </div>
);

const InfoRow: React.FC<{ label: string; value: string }> = ({ label, value }) => (
  value && (
    <div className="mb-2">
      <span className="font-medium text-gray-700 text-sm">{label}:</span>
      <p className="text-gray-600 text-sm mt-1">{value}</p>
    </div>
  )
);

const FeatureList: React.FC<{ features: string[] }> = ({ features }) => (
  <ul className="list-disc list-inside space-y-1 text-sm text-gray-600">
    {features.map((feature, index) => (
      <li key={index}>{feature}</li>
    ))}
  </ul>
);

const AddEntryForm: React.FC<{
  show: boolean;
  onClose: () => void;
  onSubmit: (entry: Omit<FungalEntry, 'id' | 'date'>) => void;
}> = ({ show, onClose, onSubmit }) => {
  const [formData, setFormData] = useState({
    scientificName: '',
    commonName: '',
    phylum: 'Ascomycota',
    class: '',
    order: '',
    family: '',
    student: '',
    habitat: '',
    substrate: '',
    macroFeatures: '',
    microFeatures: '',
    sporeDetails: '',
    reproductiveStructures: '',
    keyDiagnostic: '',
    distinguishingFeatures: '',
    mnemonic: '',
    commonMistakes: '',
    ecologicalRole: '',
    medicalRelevance: '',
    industrialUse: '',
    season: '',
    distribution: '',
    imageNotes: ''
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit({
      ...formData,
      macroFeatures: formData.macroFeatures.split(',').map(f => f.trim()).filter(f => f),
      microFeatures: formData.microFeatures.split(',').map(f => f.trim()).filter(f => f),
      keyDiagnostic: formData.keyDiagnostic.split(',').map(f => f.trim()).filter(f => f),
    });
    setFormData({
      scientificName: '',
      commonName: '',
      phylum: 'Ascomycota',
      class: '',
      order: '',
      family: '',
      student: '',
      habitat: '',
      substrate: '',
      macroFeatures: '',
      microFeatures: '',
      sporeDetails: '',
      reproductiveStructures: '',
      keyDiagnostic: '',
      distinguishingFeatures: '',
      mnemonic: '',
      commonMistakes: '',
      ecologicalRole: '',
      medicalRelevance: '',
      industrialUse: '',
      season: '',
      distribution: '',
      imageNotes: ''
    });
  };

  if (!show) return null;

  return (
    <div className="bg-white rounded-lg shadow-xl p-8 mb-6 border-l-4 border-green-600">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-green-800">Add New Fungal Identification</h2>
        <button onClick={onClose} className="text-gray-500 hover:text-gray-700 transition-colors">
          <X size={24} />
        </button>
      </div>
      
      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Form sections remain the same as original but with improved structure */}
        <div className="border-b pb-4">
          <h3 className="text-lg font-semibold text-gray-800 mb-3">Basic Taxonomy</h3>
          <div className="grid md:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Scientific Name*</label>
              <input
                type="text"
                required
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 transition-all"
                value={formData.scientificName}
                onChange={(e) => setFormData({...formData, scientificName: e.target.value})}
                placeholder="e.g., Amanita muscaria"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Common Name</label>
              <input
                type="text"
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 transition-all"
                value={formData.commonName}
                onChange={(e) => setFormData({...formData, commonName: e.target.value})}
                placeholder="e.g., Fly Agaric"
              />
            </div>
          </div>
          {/* Rest of form fields... */}
        </div>

        <button
          type="submit"
          className="w-full py-4 bg-green-600 text-white rounded-lg hover:bg-green-700 font-semibold text-lg shadow-lg transition-colors"
        >
          Add Fungal Entry
        </button>
      </form>
    </div>
  );
};

// Main Component
const FungalIDPlaylist: React.FC = () => {
  const [entries, setEntries] = useState<FungalEntry[]>(INITIAL_ENTRIES);
  const [searchTerm, setSearchTerm] = useState('');
  const [showForm, setShowForm] = useState(false);
  const [selectedPhylum, setSelectedPhylum] = useState('All');
  const [selectedHabitat, setSelectedHabitat] = useState('All');
  const [expandedEntry, setExpandedEntry] = useState<number | null>(null);
  const [sortBy, setSortBy] = useState('date');

  const handleAddEntry = (newEntryData: Omit<FungalEntry, 'id' | 'date'>) => {
    const newEntry: FungalEntry = {
      id: Date.now(),
      ...newEntryData,
      date: new Date().toISOString().split('T')[0]
    };
    setEntries([newEntry, ...entries]);
    setShowForm(false);
  };

  const deleteEntry = (id: number) => {
    setEntries(entries.filter(e => e.id !== id));
  };

  const toggleExpand = (id: number) => {
    setExpandedEntry(expandedEntry === id ? null : id);
  };

  const exportData = () => {
    const dataStr = JSON.stringify(entries, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'fungal-id-playlist.json';
    link.click();
  };

  // Filter and sort entries
  const filteredEntries = entries
    .filter(entry => {
      const matchesSearch = entry.scientificName.toLowerCase().includes(searchTerm.toLowerCase()) ||
                           entry.commonName.toLowerCase().includes(searchTerm.toLowerCase()) ||
                           entry.family.toLowerCase().includes(searchTerm.toLowerCase());
      const matchesPhylum = selectedPhylum === 'All' || entry.phylum === selectedPhylum;
      const matchesHabitat = selectedHabitat === 'All' || entry.habitat.toLowerCase().includes(selectedHabitat.toLowerCase());
      return matchesSearch && matchesPhylum && matchesHabitat;
    })
    .sort((a, b) => {
      if (sortBy === 'date') return new Date(b.date).getTime() - new Date(a.date).getTime();
      if (sortBy === 'name') return a.scientificName.localeCompare(b.scientificName);
      if (sortBy === 'phylum') return a.phylum.localeCompare(b.phylum);
      return 0;
    });

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 via-teal-50 to-emerald-50 p-6">
      <div className="max-w-7xl mx-auto">
        <Header onExport={exportData} />
        
        <SearchAndFilterBar
          searchTerm={searchTerm}
          onSearchChange={setSearchTerm}
          selectedPhylum={selectedPhylum}
          onPhylumChange={setSelectedPhylum}
          selectedHabitat={selectedHabitat}
          onHabitatChange={setSelectedHabitat}
          sortBy={sortBy}
          onSortChange={setSortBy}
          onAddEntry={() => setShowForm(true)}
        />

        <AddEntryForm
          show={showForm}
          onClose={() => setShowForm(false)}
          onSubmit={handleAddEntry}
        />

        <StatsDashboard entries={entries} />

        <div className="space-y-4">
          {filteredEntries.length === 0 ? (
            <div className="bg-white rounded-lg shadow-lg p-16 text-center text-gray-500">
              <BookOpen size={64} className="mx-auto mb-4 text-gray-400" />
              <p className="text-xl font-medium">No entries found</p>
              <p className="text-gray-400 mt-2">Try adjusting your filters or add the first specimen!</p>
            </div>
          ) : (
            filteredEntries.map(entry => (
              <EntryCard
                key={entry.id}
                entry={entry}
                isExpanded={expandedEntry === entry.id}
                onToggle={toggleExpand}
                onDelete={deleteEntry}
              />
            ))
          )}
        </div>
      </div>
    </div>
  );
};

export default FungalIDPlaylist;
