import React, { useState } from 'react';
import { Search, Plus, X, BookOpen, AlertCircle, Lightbulb, Microscope, Eye, Leaf, Download, Filter, ChevronDown, ChevronUp } from 'lucide-react';

export default function FungalIDPlaylist() {
  const [entries, setEntries] = useState([
    {
      id: 1,
      scientificName: "Aspergillus niger",
      commonName: "Black Mold",
      phylum: "Ascomycota",
      class: "Eurotiomycetes",
      order: "Eurotiales",
      family: "Aspergillaceae",
      student: "Example Entry",
      date: "2024-11-10",
      habitat: "Soil, decaying vegetation, indoor environments",
      substrate: "Various organic materials",
      macroFeatures: ["Black conidial heads visible to naked eye", "Powdery texture", "Colonies grow rapidly"],
      microFeatures: ["Septate hyphae", "Spherical vesicles", "Biseriate phialides", "Black, rough-walled conidia"],
      sporeDetails: "Globose to subglobose, 3.5-5 μm diameter, dark brown to black, echinulate",
      reproductiveStructures: "Asexual: conidiophores with vesicles bearing phialides",
      keyDiagnostic: ["Black conidiophores", "Large spherical conidial heads", "Biseriate arrangement"],
      distinguishingFeatures: "Larger, darker spore heads than A. fumigatus; black pigmentation throughout",
      mnemonic: "Niger = Black in Latin - remember the BLACK color and BLACK spores!",
      commonMistakes: "Often confused with Aspergillus fumigatus, but niger has larger, darker spore heads and black pigmentation vs. blue-green in fumigatus",
      ecologicalRole: "Saprotroph, decomposer",
      medicalRelevance: "Can cause otomycosis and pulmonary aspergillosis in immunocompromised individuals",
      industrialUse: "Produces citric acid and various enzymes for industrial use",
      season: "Year-round",
      distribution: "Cosmopolitan",
      imageNotes: "Best viewed at 400x magnification to see spore ornamentation"
    }
  ]);

  const [searchTerm, setSearchTerm] = useState('');
  const [showForm, setShowForm] = useState(false);
  const [selectedPhylum, setSelectedPhylum] = useState('All');
  const [selectedHabitat, setSelectedHabitat] = useState('All');
  const [expandedEntry, setExpandedEntry] = useState(null);
  const [sortBy, setSortBy] = useState('date');
  
  const [newEntry, setNewEntry] = useState({
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

  const phyla = ['All', 'Chytridiomycota', 'Zygomycota', 'Ascomycota', 'Basidiomycota', 'Glomeromycota'];
  const habitats = ['All', 'Soil', 'Wood', 'Leaf litter', 'Dung', 'Aquatic', 'Indoor', 'Parasitic', 'Mycorrhizal'];

  const handleSubmit = (e) => {
    e.preventDefault();
    const entry = {
      id: Date.now(),
      ...newEntry,
      macroFeatures: newEntry.macroFeatures.split(',').map(f => f.trim()).filter(f => f),
      microFeatures: newEntry.microFeatures.split(',').map(f => f.trim()).filter(f => f),
      keyDiagnostic: newEntry.keyDiagnostic.split(',').map(f => f.trim()).filter(f => f),
      date: new Date().toISOString().split('T')[0]
    };
    setEntries([entry, ...entries]);
    setNewEntry({
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
    setShowForm(false);
  };

  const deleteEntry = (id) => {
    setEntries(entries.filter(e => e.id !== id));
  };

  const toggleExpand = (id) => {
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

  let filteredEntries = entries.filter(entry => {
    const matchesSearch = entry.scientificName.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         entry.commonName.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         entry.family.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesPhylum = selectedPhylum === 'All' || entry.phylum === selectedPhylum;
    const matchesHabitat = selectedHabitat === 'All' || entry.habitat.toLowerCase().includes(selectedHabitat.toLowerCase());
    return matchesSearch && matchesPhylum && matchesHabitat;
  });

  if (sortBy === 'date') {
    filteredEntries = [...filteredEntries].sort((a, b) => new Date(b.date) - new Date(a.date));
  } else if (sortBy === 'name') {
    filteredEntries = [...filteredEntries].sort((a, b) => a.scientificName.localeCompare(b.scientificName));
  } else if (sortBy === 'phylum') {
    filteredEntries = [...filteredEntries].sort((a, b) => a.phylum.localeCompare(b.phylum));
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 via-teal-50 to-emerald-50 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-lg shadow-xl p-8 mb-6 border-t-4 border-green-600">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-4xl font-bold text-green-800 mb-2">🍄 Comprehensive Fungal ID Playlist</h1>
              <p className="text-gray-600 text-lg">A detailed collaborative database of identified fungal specimens</p>
            </div>
            <button
              onClick={exportData}
              className="px-4 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700 flex items-center gap-2"
            >
              <Download size={20} />
              Export Data
            </button>
          </div>
        </div>

        {/* Search and Filter Bar */}
        <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
          <div className="grid md:grid-cols-2 lg:grid-cols-5 gap-4">
            <div className="lg:col-span-2 relative">
              <Search className="absolute left-3 top-3 text-gray-400" size={20} />
              <input
                type="text"
                placeholder="Search by scientific name, common name, or family..."
                className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
            <select
              className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
              value={selectedPhylum}
              onChange={(e) => setSelectedPhylum(e.target.value)}
            >
              {phyla.map(p => <option key={p} value={p}>Phylum: {p}</option>)}
            </select>
            <select
              className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
              value={selectedHabitat}
              onChange={(e) => setSelectedHabitat(e.target.value)}
            >
              {habitats.map(h => <option key={h} value={h}>Habitat: {h}</option>)}
            </select>
            <button
              onClick={() => setShowForm(!showForm)}
              className="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 flex items-center gap-2 justify-center font-medium"
            >
              <Plus size={20} />
              Add Entry
            </button>
          </div>
          <div className="mt-4 flex items-center gap-4">
            <span className="text-sm text-gray-600 font-medium">Sort by:</span>
            <button
              onClick={() => setSortBy('date')}
              className={`px-3 py-1 rounded ${sortBy === 'date' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-600'}`}
            >
              Date Added
            </button>
            <button
              onClick={() => setSortBy('name')}
              className={`px-3 py-1 rounded ${sortBy === 'name' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-600'}`}
            >
              Scientific Name
            </button>
            <button
              onClick={() => setSortBy('phylum')}
              className={`px-3 py-1 rounded ${sortBy === 'phylum' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-600'}`}
            >
              Phylum
            </button>
          </div>
        </div>

        {/* Add Entry Form */}
        {showForm && (
          <div className="bg-white rounded-lg shadow-xl p-8 mb-6 border-l-4 border-green-600">
            <div className="flex justify-between items-center mb-6">
              <h2 className="text-2xl font-bold text-green-800">Add New Comprehensive Identification</h2>
              <button onClick={() => setShowForm(false)} className="text-gray-500 hover:text-gray-700">
                <X size={24} />
              </button>
            </div>
            <div className="space-y-6">
              {/* Basic Taxonomy */}
              <div className="border-b pb-4">
                <h3 className="text-lg font-semibold text-gray-800 mb-3">Basic Taxonomy</h3>
                <div className="grid md:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Scientific Name*</label>
                    <input
                      type="text"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.scientificName}
                      onChange={(e) => setNewEntry({...newEntry, scientificName: e.target.value})}
                      placeholder="e.g., Agaricus bisporus"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Common Name</label>
                    <input
                      type="text"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.commonName}
                      onChange={(e) => setNewEntry({...newEntry, commonName: e.target.value})}
                      placeholder="e.g., Button Mushroom"
                    />
                  </div>
                </div>
                <div className="grid md:grid-cols-4 gap-4 mt-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Phylum*</label>
                    <select
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.phylum}
                      onChange={(e) => setNewEntry({...newEntry, phylum: e.target.value})}
                    >
                      {phyla.filter(p => p !== 'All').map(p => <option key={p} value={p}>{p}</option>)}
                    </select>
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Class</label>
                    <input
                      type="text"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.class}
                      onChange={(e) => setNewEntry({...newEntry, class: e.target.value})}
                      placeholder="e.g., Agaricomycetes"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Order</label>
                    <input
                      type="text"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.order}
                      onChange={(e) => setNewEntry({...newEntry, order: e.target.value})}
                      placeholder="e.g., Agaricales"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Family</label>
                    <input
                      type="text"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.family}
                      onChange={(e) => setNewEntry({...newEntry, family: e.target.value})}
                      placeholder="e.g., Agaricaceae"
                    />
                  </div>
                </div>
              </div>

              {/* Habitat & Ecology */}
              <div className="border-b pb-4">
                <h3 className="text-lg font-semibold text-gray-800 mb-3">Habitat & Ecology</h3>
                <div className="grid md:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Habitat</label>
                    <input
                      type="text"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.habitat}
                      onChange={(e) => setNewEntry({...newEntry, habitat: e.target.value})}
                      placeholder="e.g., Deciduous forests, grasslands"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Substrate</label>
                    <input
                      type="text"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.substrate}
                      onChange={(e) => setNewEntry({...newEntry, substrate: e.target.value})}
                      placeholder="e.g., Wood debris, soil"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Ecological Role</label>
                    <input
                      type="text"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.ecologicalRole}
                      onChange={(e) => setNewEntry({...newEntry, ecologicalRole: e.target.value})}
                      placeholder="e.g., Saprotroph, mycorrhizal, pathogen"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Season</label>
                    <input
                      type="text"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.season}
                      onChange={(e) => setNewEntry({...newEntry, season: e.target.value})}
                      placeholder="e.g., Fall, year-round"
                    />
                  </div>
                </div>
              </div>

              {/* Morphological Features */}
              <div className="border-b pb-4">
                <h3 className="text-lg font-semibold text-gray-800 mb-3">Morphological Features</h3>
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Macroscopic Features (comma-separated)*</label>
                    <input
                      type="text"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.macroFeatures}
                      onChange={(e) => setNewEntry({...newEntry, macroFeatures: e.target.value})}
                      placeholder="e.g., White cap, brown gills, thick stipe, ring present"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Microscopic Features (comma-separated)*</label>
                    <input
                      type="text"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.microFeatures}
                      onChange={(e) => setNewEntry({...newEntry, microFeatures: e.target.value})}
                      placeholder="e.g., Septate hyphae, clamp connections, smooth spores"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Spore Details</label>
                    <textarea
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.sporeDetails}
                      onChange={(e) => setNewEntry({...newEntry, sporeDetails: e.target.value})}
                      placeholder="e.g., Ellipsoid, 8-12 x 5-7 μm, smooth, hyaline, inamyloid"
                      rows="2"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Reproductive Structures</label>
                    <textarea
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.reproductiveStructures}
                      onChange={(e) => setNewEntry({...newEntry, reproductiveStructures: e.target.value})}
                      placeholder="e.g., Basidia 4-spored, cystidia present on gill edges"
                      rows="2"
                    />
                  </div>
                </div>
              </div>

              {/* Identification Keys */}
              <div className="border-b pb-4">
                <h3 className="text-lg font-semibold text-gray-800 mb-3">Identification Keys</h3>
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Key Diagnostic Features (comma-separated)*</label>
                    <input
                      type="text"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.keyDiagnostic}
                      onChange={(e) => setNewEntry({...newEntry, keyDiagnostic: e.target.value})}
                      placeholder="e.g., Purple-brown spore print, free gills, annulus"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Distinguishing Features from Similar Species</label>
                    <textarea
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.distinguishingFeatures}
                      onChange={(e) => setNewEntry({...newEntry, distinguishingFeatures: e.target.value})}
                      placeholder="e.g., Differs from A. campestris by habitat (woodland vs. grassland) and larger spores"
                      rows="2"
                    />
                  </div>
                </div>
              </div>

              {/* Learning Aids */}
              <div className="border-b pb-4">
                <h3 className="text-lg font-semibold text-gray-800 mb-3">Learning Aids & Common Mistakes</h3>
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Mnemonic or Memory Trick</label>
                    <textarea
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.mnemonic}
                      onChange={(e) => setNewEntry({...newEntry, mnemonic: e.target.value})}
                      placeholder="Share a helpful way to remember this species..."
                      rows="2"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Common Identification Mistakes</label>
                    <textarea
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.commonMistakes}
                      onChange={(e) => setNewEntry({...newEntry, commonMistakes: e.target.value})}
                      placeholder="What species is this commonly confused with? How to tell them apart?"
                      rows="2"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Imaging Notes</label>
                    <input
                      type="text"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.imageNotes}
                      onChange={(e) => setNewEntry({...newEntry, imageNotes: e.target.value})}
                      placeholder="e.g., Best viewed at 400x, use cotton blue stain for clearer detail"
                    />
                  </div>
                </div>
              </div>

              {/* Applied Mycology */}
              <div className="border-b pb-4">
                <h3 className="text-lg font-semibold text-gray-800 mb-3">Applied Mycology</h3>
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Medical Relevance</label>
                    <textarea
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.medicalRelevance}
                      onChange={(e) => setNewEntry({...newEntry, medicalRelevance: e.target.value})}
                      placeholder="e.g., Source of antibiotics, causes disease, medicinal properties"
                      rows="2"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Industrial/Commercial Use</label>
                    <textarea
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.industrialUse}
                      onChange={(e) => setNewEntry({...newEntry, industrialUse: e.target.value})}
                      placeholder="e.g., Food production, enzyme manufacturing, bioremediation"
                      rows="2"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Geographic Distribution</label>
                    <input
                      type="text"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                      value={newEntry.distribution}
                      onChange={(e) => setNewEntry({...newEntry, distribution: e.target.value})}
                      placeholder="e.g., Cosmopolitan, North America, Europe"
                    />
                  </div>
                </div>
              </div>

              {/* Contributor Info */}
              <div>
                <h3 className="text-lg font-semibold text-gray-800 mb-3">Contributor Information</h3>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">Your Name*</label>
                  <input
                    type="text"
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500"
                    value={newEntry.student}
                    onChange={(e) => setNewEntry({...newEntry, student: e.target.value})}
                    placeholder="Your name"
                  />
                </div>
              </div>

              <button
                onClick={handleSubmit}
                className="w-full py-4 bg-green-600 text-white rounded-lg hover:bg-green-700 font-semibold text-lg shadow-lg"
              >
                Add Comprehensive Entry to Playlist
              </button>
            </div>
          </div>
        )}

        {/* Stats Dashboard */}
        <div className="grid grid-cols-2 md:grid-cols-5 gap-4 mb-6">
          <div className="bg-white rounded-lg shadow-lg p-4 text-center border-t-4 border-green-500">
            <div className="text-3xl font-bold text-green-600">{entries.length}</div>
            <div className="text-sm text-gray-600 font-medium">Total Species</div>
          </div>
          <div className="bg-white rounded-lg shadow-lg p-4 text-center border-t-4 border-blue-500">
            <div className="text-3xl font-bold text-blue-600">{new Set(entries.map(e => e.phylum)).size}</div>
            <div className="text-sm text-gray-600 font-medium">Phyla</div>
          </div>
          <div className="bg-white rounded-lg shadow-lg p-4 text-center border-t-4 border-purple-500">
            <div className="text-3xl font-bold text-purple-600">{entries.filter(e => e.mnemonic).length}</div>
            <div className="text-sm text-gray-600 font-medium">Memory Tricks</div>
          </div>
          <div className="bg-white rounded-lg shadow-lg p-4 text-center border-t-4 border-orange-500">
            <div className="text-3xl font-bold text-orange-600">{entries.filter(e => e.commonMistakes).length}</div>
            <div className="text-sm text-gray-600 font-medium">Mistake Alerts</div>
          </div>
          <div className="bg-white rounded-lg shadow-lg p-4 text-center border-t-4 border-teal-500">
            <div className="text-3xl font-bold text-teal-600">{new Set(entries.map(e => e.student)).size}</div>
            <div className="text-sm text-gray-600 font-medium">Contributors</div>
          </div>
        </div>

        {/* Entries List */}
        <div className="space-y-4">
          {filteredEntries.length === 0 ? (
            <div className="bg-white rounded-lg shadow-lg p-16 text-center text-gray-500">
              <BookOpen size={64} className="mx-auto mb-4 text-gray-400" />
              <p className="text-xl font-medium">No entries found</p>
              <p className="text-gray-400 mt-2">Try adjusting your filters or be the first to add a specimen!</p>
            </div>
          ) : (
            filteredEntries.map(entry => (
              <div key={entry.id} className="bg-white rounded-lg shadow-lg hover:shadow-xl transition-all">
                {/* Entry Header */}
                
