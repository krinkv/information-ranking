import {Component} from '@angular/core';
import {SpellcheckingService} from "../../services/spellchecking.service";
import {Router} from "@angular/router";

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
  algorithm: string = 'tf-idf';

  constructor(private spellcheckingService: SpellcheckingService,
              private router: Router) {
  }

  onSubmit() {
    this.router.navigate(['/search-result', {data: this.inputValue, algorithm: this.algorithm}])
  }

  onCorrect() {
    this.inputValue = this.inputValue.trim();
    let index = this.inputValue.lastIndexOf(' ');
    let correctQuery = this.inputValue.substring(0, index);
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

  changeAlgorithm() {
    if (this.algorithm === 'nlp') {
      this.algorithm = 'tf-idf';
    } else {
      this.algorithm = 'nlp';
    }
  }
}
