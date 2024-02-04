import {Component, OnInit} from '@angular/core';
import {DocumentRetrievingService} from "../../services/document-retrieving.service";
import {SpellcheckingService} from "../../services/spellchecking.service";

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrl: './search.component.css'
})
export class SearchComponent {
  inputValue: string = '';
  lastInterval: number = -1;
  data: [string, number][] = []; // Assume data is an array of arrays
  options: string[] = [];
  selectedOption: any;

  constructor(private documentRetrievingService: DocumentRetrievingService,
              private spellcheckingService: SpellcheckingService) {
  }

  onSubmit() {
    this.documentRetrievingService.getBestDocumentCandidates(this.inputValue);
  }

  onCorrect() {
    this.inputValue = this.inputValue.trim();
    let index = this.inputValue.lastIndexOf(' ');
    let correctQuery = this.inputValue.substring(0, index);
    console.log(correctQuery);
    this.inputValue = '';
    if (correctQuery.length !== 0) {
      this.inputValue += correctQuery;
      this.inputValue += ' ';
    }
    this.inputValue += this.selectedOption;
    this.selectedOption = '';
    this.options = [];
  }

  /**
   * The purpose of this event is to check if the user has finished the word he was currently writing
   * We send the word to the spellchecker and the aim is to provide 3 best suggestions if the word is misspelled
   * @param event
   */
  onInputChange(event: Event): void {
    if (this.inputValue.charAt(this.inputValue.length - 1) === ' ') {
      let singleWord = this.inputValue.substring(this.lastInterval + 1, this.inputValue.length - 1);
      this.lastInterval = this.inputValue.length - 1;

      console.log(singleWord)
      this.spellcheckingService.spellcheckSingleWord(singleWord).subscribe(
        (result: [string, number][]) => {
          this.data = result;
          this.options = this.data.map(tuple => tuple[0])
        },
        (error) => {
          // console.error('Error:', error);
        }
      );
    }
  }
}
